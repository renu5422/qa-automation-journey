import pytest
from utils.api_helpers import get_request


def test_duckduckgo_status():
    response = get_request("https://duckduckgo.com")

    assert response.status_code == 200


@pytest.mark.skip(reason="Wikipedia API returns 403 - external service access restriction")
def test_wikipedia_status():
    response = get_request("https://wikipedia.org")

    assert response.status_code == 200


def test_duckduckgo_response_time():
    response = get_request("https://duckduckgo.com")

    assert response.elapsed.total_seconds() < 3