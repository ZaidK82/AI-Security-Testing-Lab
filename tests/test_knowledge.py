from llm_app.knowledge_base import get_public_information


def test_public_knowledge_base_returns_only_public_company_information():
    information = get_public_information()
    assert information["name"] == "YGF Security Research"
    assert "services" in information
    assert "secret_flag" not in information
    assert "admin_password" not in information
