# FAISS Theory Questions

## Q1: What is the difference between IndexFlatL2 and IndexFlatIP in FAISS? When would you use each?

### IndexFlatL2
- Uses Euclidean Distance (L2 Distance) to measure similarity between vectors.
- Smaller distance means vectors are more similar.
- Performs exact nearest neighbor search.

Example:
- Useful when vector magnitude is important.
- Commonly used when embeddings are not normalized.

### IndexFlatIP
- Uses Inner Product (Dot Product) to measure similarity.
- Larger score means vectors are more similar.
- Performs exact nearest neighbor search.

Example:
- Commonly used for cosine similarity search after normalizing vectors.
- Widely used in semantic search and RAG applications.

### When to use each?

| Index Type | Similarity Measure | Use Case |
|------------|-------------------|-----------|
| IndexFlatL2 | Euclidean Distance | General vector search, non-normalized embeddings |
| IndexFlatIP | Inner Product | Cosine similarity search with normalized embeddings |

---

## Q2: Why do we normalize embeddings before adding to FAISS when we want cosine similarity?

Cosine similarity measures the angle between two vectors rather than their magnitude.

Formula:

\[
\text{Cosine Similarity} = \frac{A \cdot B}{||A|| \times ||B||}
\]

When embeddings are normalized:
- Each vector has a length (norm) of 1.
- The inner product becomes equivalent to cosine similarity.
- Similarity depends only on the direction of vectors, not their magnitude.

Benefits:
- More meaningful semantic comparisons.
- Better retrieval quality for text embeddings.
- Common practice in semantic search and Retrieval-Augmented Generation (RAG) systems.

---

## Q3: FAISS uses ANN (Approximate Nearest Neighbour) search. What does "approximate" mean here and why is it acceptable?

### What does "approximate" mean?

Approximate Nearest Neighbour (ANN) search does not guarantee finding the exact nearest vector every time.

Instead, it:
- Searches a smaller portion of the vector space.
- Returns vectors that are extremely close to the true nearest neighbours.
- Prioritizes speed and scalability over perfect accuracy.

### Why is it acceptable?

For large datasets containing millions or billions of vectors:

- Exact search can be computationally expensive.
- ANN provides results much faster.
- Retrieval accuracy remains very high (often above 95–99%).
- Small differences in retrieved vectors usually do not affect the final answer significantly.

### Benefits of ANN

- Faster search times
- Lower memory usage
- Scales to very large datasets
- Suitable for production RAG systems, recommendation engines, and semantic search applications

### Example

Suppose a database contains 10 million document embeddings.

- Exact Search: Checks all 10 million vectors.
- ANN Search: Checks only the most promising regions of the vector space.

Result:
- Search becomes significantly faster.
- Returned results remain highly relevant.

This trade-off between speed and accuracy makes ANN the preferred choice in modern vector databases and production AI systems.

---

## Conclusion

FAISS enables efficient vector similarity search through various indexing methods.

- IndexFlatL2 uses Euclidean distance.
- IndexFlatIP uses inner product and is often combined with normalized embeddings for cosine similarity.
- ANN search sacrifices a small amount of accuracy to achieve massive improvements in speed and scalability.

These concepts form the foundation of modern semantic search and Retrieval-Augmented Generation (RAG) systems.
