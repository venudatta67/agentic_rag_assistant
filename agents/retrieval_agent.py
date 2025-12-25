class RetrievalAgent:
    def __init__(self, index, embedder):
        self.index = index
        self.embedder = embedder

    def retrieve(self, query, section=None, top_k=5):
        query_vec = self.embedder.embed([query])[0]
        results = self.index.search(query_vec, top_k)

        if section:
            results = [
                r for r in results if section.lower() in r["section"].lower()
            ]

        return results
