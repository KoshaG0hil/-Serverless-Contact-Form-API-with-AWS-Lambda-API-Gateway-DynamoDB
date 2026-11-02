import json
import pytest
from cli import simulate_submit, simulate_get, MOCK_DYNAMODB


@pytest.fixture(autouse=True)
def clean_db():
    MOCK_DYNAMODB.clear()


def test_submit_success():
    res = simulate_submit("Kosha", "kosha@example.com", "Hello from test")
    assert res["statusCode"] == 200
    body = json.loads(res["body"])
    assert "Hi Kosha, your message has been saved!" in body["message"]
    assert len(MOCK_DYNAMODB) == 1


def test_submit_missing_fields():
    res = simulate_submit("", "kosha@example.com", "Missing name")
    assert res["statusCode"] == 400
    body = json.loads(res["body"])
    assert "error" in body


def test_get_submissions():
    simulate_submit("User 1", "u1@test.com", "Msg 1")
    simulate_submit("User 2", "u2@test.com", "Msg 2")

    get_res = simulate_get()
    assert get_res["statusCode"] == 200
    items = json.loads(get_res["body"])["messages"]
    assert len(items) == 2
    assert items[0]["email"] == "u1@test.com"
    assert items[1]["email"] == "u2@test.com"
