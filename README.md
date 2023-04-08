# Wayback Robots
Wayback Robots is a Python tool that extracts information from robots.txt files archived in the Wayback Machine for specified domains.

## Installation
###Requirements
- Python 3.6 or higher
- pip (for installing dependencies)
##Installing Dependencies
Clone the repository:
```
git clone https://github.com/yourusername/wayback-robots.git
cd wayback-robots
```

Install the dependencies:
```
pip install -r requirements.txt
```

## Usage
To use the tool, follow these steps:

1) Run the wayback_robots.py script:
```
python wayback.py
```
2) Enter the domains you want to fetch robots.txt information for, one per line, and press `Enter` after each domain. When you're done entering domains, press `Ctrl-D` (Linux/Mac) or `Ctrl-Z` (Windows) to start processing.
Example input:

```
example.com
example.org
```
3) The results will be printed to the screen as the domains are processed.

## How it Works
The tool performs the following actions for each entered domain:

1) Requests the list of robots.txt files for the specified domain from the Wayback Machine.
2) For each found robots.txt file, requests its content.
3) Extracts paths from the robots.txt file content and prints them to the screen.

Multithreading is used to process multiple domains concurrently, increasing the efficiency of the tool.
