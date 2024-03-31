#!/usr/bin/env python3
import sys
import math

document_vectors = {}
for line in sys.stdin:
    type_, data = line.strip().split('\t', 1)
    if type_ == 'doc':
        doc_id, vector_str = data.split('\t', 1)
        document_vectors[doc_id] = eval(vector_str)
    elif type_ == 'query':
        query_vector = eval(data)

def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    norm1 = math.sqrt(sum(v1 ** 2 for v1 in vec1))
    norm2 = math.sqrt(sum(v2 ** 2 for v2 in vec2))
    return dot_product / (norm1 * norm2)

similarity_scores = {}
for doc_id, doc_vector in document_vectors.items():
    similarity_scores[doc_id] = cosine_similarity(query_vector, doc_vector)

for doc_id, score in similarity_scores.items():
    print(f"{doc_id}\t{score}")
