#!/usr/bin/env python3
import sys

current_document = None
current_tf_idf_vector = []

for line in sys.stdin:
    document_id, term_index, tf_idf = line.strip().split('\t')
    term_index = int(term_index)
    tf_idf = float(tf_idf)
    
    if current_document == document_id:
        current_tf_idf_vector.append((term_index, tf_idf))
    else:
        if current_document:
            print(f"{current_document}\t{current_tf_idf_vector}")
        current_document = document_id
        current_tf_idf_vector = [(term_index, tf_idf)]

if current_document:
    print(f"{current_document}\t{current_tf_idf_vector}")
