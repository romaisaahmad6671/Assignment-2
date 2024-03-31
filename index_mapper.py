#!/usr/bin/env python3
import sys
import csv
import math

idf_values = {}
with open('idf_values.txt', 'r') as idf_file:
    for line in idf_file:
        term, idf = line.strip().split('\t')
        idf_values[term] = float(idf)

vocabulary = list(idf_values.keys())

def calculate_tf_idf(document_id, text):
    tf_vector = {}
    words = text.lower().split()
    total_words = len(words)
    for word in words:
        if word in idf_values:
            tf_vector[word] = tf_vector.get(word, 0) + 1 / total_words  # Calculate TF
    tf_idf_vector = [(vocabulary.index(term), tf * idf_values[term]) for term, tf in tf_vector.items()]
    return document_id, tf_idf_vector

csv_reader = csv.reader(sys.stdin)
for row in csv_reader:
    if len(row) >= 2:
        document_id, text = row[0], row[1]
        document_id, tf_idf_vector = calculate_tf_idf(document_id, text)
        for term_index, tf_idf in tf_idf_vector:
            print(f"{document_id}\t{term_index}\t{tf_idf}")
