import requests

class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "embedding": [0.1] * 768,
            "response": "Verdict: PASS\nExplanation: Good tone"
        }

def fake_post(*args, **kwargs):
    return FakeResponse()

requests.post = fake_post

import sys
from tests.fakes import FakeCollection

# Replace vector_db before app imports it
fake = FakeCollection()

fake_vector_db = type("x", (), {"collection": fake})

sys.modules["app.vector_db"] = fake_vector_db
