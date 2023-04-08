# Wayback Robots
Wayback Robots is a Python tool that extracts information from robots.txt files archived in the Wayback Machine for specified domains.

## Installation
Requirements
- Python 3.6 or higher
- pip (for installing dependencies)

## Installing Dependencies
Clone the repository:
```
git clone https://github.com/elizarfish/wayback.git
cd wayback
```

Install the dependencies:
```
pip install -r requirements.txt
```

## Usage
To use the tool, create a text file with the domains you want to fetch robots.txt information for, one per line. Then, run the script with the following command:
```
python script.py -f input_domains.txt -o output.txt
```

Replace `input_domains.txt` with the name of your input file containing the list of domains and `output.txt` with the desired output file name.

## How it Works
The tool performs the following actions for each entered domain:

1) Requests the list of robots.txt files for the specified domain from the Wayback Machine.
2) For each found robots.txt file, requests its content.
3) Extracts paths from the robots.txt file content and appends them to the output file.

Multithreading is used to process multiple domains concurrently, increasing the efficiency of the tool.
