def test_duckduckgo_search(page):
    page.goto("https://duckduckgo.com")

    search_input = page.locator('input[name="q"]')
    search_input.fill("Playwright automation")

    page.keyboard.press("Enter")

    page.wait_for_selector("h2")

    assert page.locator("h2").first.is_visible()
