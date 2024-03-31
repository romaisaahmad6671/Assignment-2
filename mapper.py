#!/usr/bin/env python3
import sys
import csv

# Assuming your CSV data is passed to stdin, this will read it line by line
csv_reader = csv.reader(sys.stdin)
seen = set()  # To keep track of words already seen in the current document for DF calculation

for row in csv_reader:
    if len(row) < 2:  # Skip lines that don't have at least two columns
        continue
    document_id, text = row[0], row[1]
    words = text.split()
    seen.clear()

    for word in words:
        word = word.lower()  # Normalize to lowercase
        # Emit for TF calculation
        print(f"TF\t{word}\t{document_id}\t1")
        # For DF, only emit once per document per word
        if word not in seen:
            print(f"DF\t{word}\t1")
            seen.add(word)
