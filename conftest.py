import pytest

from config.settings import BASE_URL


@pytest.fixture
def base_url() -> str:
    return BASE_URL
