import json
import re
import requests
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

def fetch_robots_txt(domain, output_file):
    try:
        url = f"http://web.archive.org/cdx/search/cdx?url={domain}/robots.txt&output=json"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error fetching robots.txt for {domain}: {response.status_code}")
            return

        records = response.json()
        unique_paths = set()

        if len(records) >= 1:
            for record in records[1:]:
                timestamp = record[1]
                wayback_url = f"http://web.archive.org/web/{timestamp}if_/{record[2]}"
                resp = requests.get(wayback_url)

                if resp.status_code == 200:
                    body = resp.text
                    path_pattern = re.compile(r"/[\w\-./?=]*")
                    path_matches = path_pattern.findall(body)

                    for path in path_matches:
                        unique_paths.add(path)

        with open(output_file, "a") as f:
            for path in unique_paths:
                f.write(f"{domain} {path}\n")

        print(f"Successfully fetched and wrote paths for {domain}")

    except Exception as e:
        print(f"An error occurred while processing {domain}: {e}")

def worker(domain_queue, output_file):
    while not domain_queue.empty():
        domain = domain_queue.get()
        fetch_robots_txt(domain, output_file)
        domain_queue.task_done()
        print(f"Finished processing {domain}")

def main():
    parser = argparse.ArgumentParser(description="Wayback Machine robots.txt fetcher")
    parser.add_argument("-f", "--file", required=True, help="Input file containing domain list")
    parser.add_argument("-o", "--output", required=True, help="Output file to save results")
    args = parser.parse_args()

    domain_queue = Queue()

    with open(args.file, "r") as f:
        for line in f:
            domain_queue.put(line.strip())

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(worker, domain_queue, args.output) for _ in range(20)]
        for future in futures:
            future.result()  # This will raise an exception if any occurred within a thread

    print("All work has been processed.")

if __name__ == "__main__":
    main()
