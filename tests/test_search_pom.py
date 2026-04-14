from pages.search_page import SearchPage


def test_search_results_with_pom(page):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search("Playwright automation")

    count = search_page.get_results_count()

    assert count >= 5
