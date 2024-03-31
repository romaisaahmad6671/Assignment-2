#!/usr/bin/env python3
import sys
import math


total_documents = 50

current_word = None
current_count = 0
calc_type = None  
df_counts = {}  
for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) not in [3, 4]:
        continue  

    if len(parts) == 4:  
        prefix, word, doc_id, count = parts
        if prefix != "TF":
            continue  
    else:  
        prefix, word, count = parts
        doc_id = None  
    try:
        count = int(count)
    except ValueError:
        continue  
    if word != current_word or (prefix == "DF" and calc_type != "DF"):
        if current_word and calc_type == "DF":
            df_counts[current_word] = current_count
        current_count = count
        current_word = word
        calc_type = prefix
    else:
        current_count += count

if current_word and calc_type == "DF":
    df_counts[current_word] = current_count

print("Term\tIDF")
for term, df in df_counts.items():
    if df > 0 and df <= total_documents:
        idf = math.log10(total_documents / df)
        print(f"{term}\t{idf}")
    else:
        print(f"Error: Invalid DF={df} for term '{term}' - Skipping term", file=sys.stderr)
