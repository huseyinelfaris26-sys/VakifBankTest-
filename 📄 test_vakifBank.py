import pytest
from vakifBank import VakifClient

@pytest.fixture
def client():
    return VakifClient(api_key="FAKE_KEY")

def test_get_balance(client):
    """
    Simple smoke-test that the API returns a dict with a 'balance' field.
    """
    result = client.get_balance(account_id=12345)
    assert isinstance(result, dict)
    assert "balance" in result
    assert result["balance"] >= 0
