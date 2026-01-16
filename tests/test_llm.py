from app.llm import llm_review

def test_pass():
    r = llm_review("bold", "great text", 0.9)
    assert "PASS" in r

def test_fail():
    r = llm_review("bold", "bad text", 0.1)
    assert "PASS" in r or "FAIL" in r

