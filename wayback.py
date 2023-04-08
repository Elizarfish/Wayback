import json
import re
import requests
import sys
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

def fetch_robots_txt(domain):
    url = f"http://web.archive.org/cdx/search/cdx?url={domain}/robots.txt&output=json"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    records = response.json()

    if len(records) >= 1:
        for record in records[1:]:
            timestamp = record[1]
            wayback_url = f"http://web.archive.org/web/{timestamp}if_/{record[2]}"
            resp = requests.get(wayback_url)

            if resp.status_code >= 200 and resp.status_code <= 200:
                body = resp.text
                path_pattern = re.compile(r"/[\w\-./?=]*")
                path_matches = path_pattern.findall(body)

                for path in path_matches:
                    print(path)

def worker(domain_queue):
    while not domain_queue.empty():
        domain = domain_queue.get()
        fetch_robots_txt(domain)

def main():
    domain_queue = Queue()

    for line in sys.stdin:
        domain_queue.put(line.strip())

    with ThreadPoolExecutor(max_workers=20) as executor:
        for _ in range(20):
            executor.submit(worker, domain_queue)

if __name__ == "__main__":
    main()
