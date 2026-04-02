#!/usr/bin/python3
import sys

total_size = 0
count = 0
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {code: 0 for code in status_codes}

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 2:
            try:
                total_size += int(parts[-1])
            except:
                pass

            code = parts[-2]
            if code in stats:
                stats[code] += 1

        count += 1
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

print_stats()
