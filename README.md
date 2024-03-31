# Developing a Naive Search Engine Utilising MapReduce Technology:

This repository hosts a small-scale search engine developed using MapReduce technology. Built as part of an assignment for the Fundamental of Big Data Analytics (DS2004) course for distributed systems, it efficiently indexes and searches large datasets.

## Dependencies

* Ubuntu ([install](https://ubuntu.com/download))
* Hadoop ([install](https://hadoop.apache.org/docs/r3.3.1/hadoop-project-dist/hadoop-common/SingleCluster.html))
* Python ([install](https://www.python.org/downloads/))
* Jupyter Notebook ([install](https://docs.jupyter.org/en/latest/install.html))
* pandas ([install](https://pandas.pydata.org/docs/getting_started/install.html))
* nltk ([install](https://www.nltk.org/install.html))
* NumPy ([install](https://numpy.org/install/))


## Project Overview:

This project is a simplified yet powerful implementation of a search engine using the Hadoop MapReduce framework. It indexes a subset of English Wikipedia articles to allow efficient query processing and retrieval based on TF-IDF (Term Frequency-Inverse Document Frequency) scores. The goal is to demonstrate the application of big data technologies in information retrieval systems.

## Dataset
We use a subset of the English Wikipedia dump, which includes approximately 5 million articles. Each article is structured with fields for ARTICLE_ID, TITLE, SECTION_TITLE, and SECTION_TEXT. The dataset is sourced from [Wikimedia's download page](https://drive.google.com/file/d/1lGVGqzF5CNWaoV-zoz8_mlThvHwMgcsP/view?usp=sharing).

## Theoretical Framework and Methodology

### Data Preprocessing
Before delving into the core functionalities of our search engine, the first crucial step involves preprocessing the English Wikipedia dataset. This phase is dedicated to cleansing and standardizing the text, which includes removing irrelevant characters, standardizing formats, and segmenting texts into processable units. This preprocessing not only ensures the integrity and uniformity of the data but also significantly enhances the efficiency of subsequent operations by eliminating noise from the dataset.

### Term Frequency (TF) Computation
Following preprocessing, we focus on the computation of Term Frequency (TF) for each word within the documents. TF is a measure that quantifies the number of times a term appears in a document relative to the length of that document. This step is fundamental in identifying the significance of each term within individual documents, setting the stage for the next critical phase of our methodology.

### Inverse Document Frequency (IDF) Calculation
The Inverse Document Frequency (IDF) calculation comes next, where we determine the IDF for each term across the entire dataset. IDF is calculated as the logarithmically scaled inverse fraction of the documents that contain the word, obtaining a measure that decreases with the number of documents that contain the term. This calculation aims to diminish the weight of terms that occur very frequently across the corpus and are hence less informative.

### Document Index Construction
Armed with TF and IDF values, we proceed to construct the document index. This structured index is essentially a map that associates terms with their corresponding documents and TF-IDF scores. The construction of this index is a pivotal moment in our project, as it enables the search engine to quickly retrieve relevant documents based on the terms they contain. The index is optimized for efficient lookup, drastically reducing the time required to process queries.

### Query Processing
The final stage of our methodology is query processing. In this phase, we vectorize input queries using the same TF-IDF model applied to the documents in our corpus. By calculating the cosine similarity between the query vector and document vectors in our index, we can assess the relevance of each document to the query. Documents with higher cosine similarity scores are deemed more relevant to the query, thus forming the basis of our search engine's response to user inquiries.


## Implementation Details

### MapReduce Jobs
1. **Indexing Job**: 
   - **Mapper**: Processes each document, extracting words and computing term frequencies (TF).
   - **Reducer**: Aggregates term frequencies and computes document frequencies (DF) and TF-IDF values for each term in each document.

2. **Query Processing Job**: 
   - **Mapper**: Processes the query, converting it into a vector using IDF values.
   - **Reducer**: Computes the cosine similarity between the query vector and document vectors, ranking documents based on relevance.

### Files and Scripts
- `mapper.py`: Extracts terms and computes TF.
- `reducer.py`: Aggregates TF and computes DF and TF-IDF.
- `idf.py`: Pre-processes documents to compute IDF for each term.
- `query_mapper.py` and `query_reducer.py`: Process search queries and calculate relevance scores.
- `index_mapper.py` and `index_reducer.py`: Specific mappers and reducers for indexing tasks.



## Usage

### Indexing
Run the indexing job on Hadoop with your dataset to generate the index:

```
hadoop jar /path/to/hadoop-streaming.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /path/to/input/files \
-output /path/to/output/index
```

### Querying
Execute a query by running another MapReduce job, specifying the query text:

```
hadoop jar /path/to/hadoop-streaming.jar \
-file query_mapper.py -mapper "query_mapper.py 'your search query here'" \
-file query_reducer.py -reducer query_reducer.py \
-input /path/to/index/output \
-output /path/to/query/results
```

## Contributors:

This project exists thanks to the extraordinary people who contributed to it.
* **[Sharjeel Nadir](i212699@nu.edu.pk)**
* **[Masroor Bin Rehan](i211707@nu.edu.pk)**

---

### References:

* https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredCommands.html
* https://www.alachisoft.com/resources/docs/ncache/prog-guide/mapreduce-overview.html
* https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html

## Notes
- This project is a part of the coursework for Fundamental of Big Data Analytics (DS2004).
- Ensure your Hadoop environment is properly configured before executing MapReduce jobs.
- For detailed configuration and setup of Apache Hadoop, refer to the official [Apache Hadoop documentation](https://hadoop.apache.org/docs/stable/).
