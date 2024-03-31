
import csv
from collections import defaultdict, Counter
import math

#using for test data set ignore if not required

file_path = 'first_50_rows.csv'  # Adjust to your actual file path

tf_counts = defaultdict(Counter)  # TF counts per document
df_counts = Counter()  # DF counts

# Read the CSV and populate TF and DF structures
with open(file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if len(row) < 2:
            continue
        document_id, text = row[0], row[1]
        words = text.lower().split()
        seen = set()
        for word in words:
            tf_counts[document_id][word] += 1
            if word not in seen:
                df_counts[word] += 1
                seen.add(word)

# Assuming total number of documents is known
total_documents = len(tf_counts)

# Calculate IDF
idf_values = {term: math.log10(total_documents / df) for term, df in df_counts.items()}

# Create vocabulary with unique IDs
vocabulary = sorted(df_counts.keys())
vocab_with_ids = {term: i for i, term in enumerate(vocabulary)}

# Print TF in the requested format
print("Term Frequency (TF):")
for doc_id, counts in tf_counts.items():
    print(f"Document {doc_id}:")
    for term, count in counts.items():
        term_id = vocab_with_ids[term]
        print(f"({term_id}, {count})", end=", ")
    print("\n")

# Print IDF in the requested format
print("\nInverse Document Frequency (IDF):")
for term, idf in sorted(idf_values.items(), key=lambda x: vocab_with_ids[x[0]]):
    term_id = vocab_with_ids[term]
    print(f"({term_id}, {idf:.2f})", end=", ")
print()
