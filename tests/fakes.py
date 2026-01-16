class FakeCollection:
    def __init__(self):
        self.rows = []

    def add(self, ids, embeddings, metadatas):
        for i in range(len(ids)):
            self.rows.append({
                "id": ids[i],
                "embedding": embeddings[i],
                "metadata": metadatas[i]
            })

    def get(self, include=None, where=None):
        if where:
            result = [r["metadata"] for r in self.rows if r["metadata"]["brand_name"] == where["brand_name"]]
        else:
            result = [r["metadata"] for r in self.rows]

        return {"metadatas": result}

    def query(self, query_embeddings, where, n_results):
        matches = [r for r in self.rows if r["metadata"]["brand_name"] == where["brand_name"]]

        return {
            "distances": [[0.2]],
            "metadatas": [[matches[0]["metadata"]]]
        }
