from app.tone_service import create_brand, get_brand, check_tone

def test_create_and_get_brand():
    brand_id = create_brand("Nike", ["bold"], ["Just do it"])
    brand = get_brand("Nike")
    assert brand["brand_name"] == "Nike"


def test_check_tone():
    create_brand("Tesla", ["innovative"], ["Future of cars"])
    r = check_tone("Tesla", "Amazing future car")
    assert "llm_result" in r
