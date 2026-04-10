def test_duckduckgo_results_count(page):
    page.goto("https://duckduckgo.com")

    search_input = page.locator('input[name="q"]')
    search_input.fill("Playwright automation")
    page.keyboard.press("Enter")

    page.wait_for_selector("h2")

    results = page.locator("h2")
    count = results.count()

    print("Results count:", count)

    assert count >= 5
    assert "Playwright" in page.title()
