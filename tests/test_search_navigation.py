from pages.search_page import SearchPage
from utils.test_data import SEARCH_QUERIES


def test_duckduckgo_navigation(page):
    search_page = SearchPage(page)

    # Open search engine
    search_page.goto()

    # Perform search
    search_page.search(
        SEARCH_QUERIES["basic"]
    )

    # Wait for results
    search_page.wait_for_results()

    # Click first result
    search_page.click_first_result()

    # Wait for correct title
    search_page.wait_for_page_title(
        "Playwright"
    )

    # Final validation
    assert "Playwright" in page.title()