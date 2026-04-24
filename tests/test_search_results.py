from pages.search_page import SearchPage
from utils.test_data import SEARCH_QUERIES
from utils.wait_helpers import take_screenshot


def test_search_results(page):
    search_page = SearchPage(page)

    # Complete search flow
    search_page.search_and_wait(
        SEARCH_QUERIES["basic"]
    )

    # Validate results loaded
    assert search_page.is_results_loaded(), (
        "Search results did not load"
    )

    # Validate correct title
    assert "Playwright" in page.title(), (
        "Incorrect page title"
    )

    # Capture screenshot
    take_screenshot(
        page,
        "search_results"
    )


def test_search_results_count(page):
    search_page = SearchPage(page)

    # Complete search flow
    search_page.search_and_wait(
        SEARCH_QUERIES["basic"]
    )

    # Get results count
    count = search_page.get_results_count()

    print("Results count:", count)

    # Validate results count
    assert count >= 5, (
        "Less than expected results"
    )