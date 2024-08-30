#!/usr/bin/python3
import sys
import signal
import re

"""
Log Parsing Script
This script reads lines from stdin, parses them to extract specific metrics
and prints statistics.
"""

# Global variables to store the aggregated data
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

# Regular expression to match the log line format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1\.1" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)


def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line):
    """Processes a single line of log and updates global metrics."""
    global total_size

    match = log_pattern.match(line)
    if match:
        status = match.group("status")
        size = int(match.group("size"))

        total_size += size
        if status in status_codes:
            status_codes[status] += 1


def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) to print statistics."""
    print_statistics()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Main loop to process stdin line by line
line_count = 0

try:
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1

        if line_count == 10:
            print_statistics()
            line_count = 0

    print_statistics()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
