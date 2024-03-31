#!/usr/bin/env python3
import sys
import math

idf_values = {}
with open('idf_values.txt', 'r') as idf_file:
    for line in idf_file:
        term, idf = line.strip().split('\t')
        idf_values[term] = float(idf)

vocabulary = list(idf_values.keys())

def calculate_query_vector(query):
    query_vector = [0] * len(idf_values)
    words = query.lower().split()
    total_words = len(words)
    for word in words:
        if word in idf_values:
            query_vector[vocabulary.index(word)] += 1 / total_words  # Calculate TF
    return query_vector

for line in sys.stdin:
    query = line.strip()
    query_vector = calculate_query_vector(query)
    print(f"query\t{query_vector}")
