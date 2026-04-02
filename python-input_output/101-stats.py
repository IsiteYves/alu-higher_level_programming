#!/usr/bin/python3
import sys


total_size = 0
line_count = 0
valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {code: 0 for code in valid_codes}


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in stats:
                stats[status_code] += 1

            try:
                total_size += int(file_size)
            except ValueError:
                pass

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

print_stats()
