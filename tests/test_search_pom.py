from config.settings import DEFAULT_SEARCH_TERM
from pages.search_page import SearchPage
from utils.helpers import HelperUtils


def test_search_results_with_pom(page):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search(DEFAULT_SEARCH_TERM)

    count = search_page.get_results_count()

    HelperUtils.take_screenshot(page, "search_results")

    assert count >= 5
