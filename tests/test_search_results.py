from pages.search_page import SearchPage


def test_google_title(page):
    page.goto("https://www.google.com")

    assert "Google" in page.title()


def test_duckduckgo_search(page):
    page.goto("https://duckduckgo.com")

    search_input = page.locator('input[name="q"]')
    search_input.fill("Playwright automation")

    page.keyboard.press("Enter")

    page.wait_for_selector('[data-testid="result"]')

    assert page.locator('[data-testid="result"]').first.is_visible()


def test_duckduckgo_results_count(page):
    page.goto("https://duckduckgo.com")

    search_input = page.locator('input[name="q"]')
    search_input.fill("Playwright automation")
    page.keyboard.press("Enter")

    page.wait_for_selector('[data-testid="result"]')

    results = page.locator('[data-testid="result"]')
    count = results.count()

    print("Results count:", count)

    assert count >= 5
    assert "Playwright" in page.title()


def test_search_results_with_pom(page):
    search_page = SearchPage(page)

    search_page.goto()
    search_page.search("Playwright")
    search_page.wait_for_results()

    assert search_page.is_results_loaded(), "Results did not load properly"
