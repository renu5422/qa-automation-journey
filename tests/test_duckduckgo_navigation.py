def test_duckduckgo_navigation(page):
    page.goto("https://duckduckgo.com")

    search_input = page.locator('input[name="q"]')
    search_input.fill("Playwright automation")
    page.keyboard.press("Enter")

    page.wait_for_selector("h2")

    page.locator("h2").first.click()

    page.wait_for_load_state("load")

    assert "Playwright" in page.title()
