from app.embeddings import get_embedding

def test_embedding():
    v = get_embedding("hello")
    assert len(v) == 768
