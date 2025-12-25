import faiss
import numpy as np

class VectorIndex:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, embeddings, metadata):
        self.index.add(np.array(embeddings).astype("float32"))
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )
        results = []
        for idx, score in zip(I[0], D[0]):
            results.append({
                **self.metadata[idx],
                "score": float(score)
            })
        return results
