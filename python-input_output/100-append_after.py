#!/usr/bin/python3
"""Inserts a line of text to a file after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends new_string after lines containing search_string"""
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
