from playwright.sync_api import sync_playwright

def test_google_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        search_input = page.locator('textarea[name="q"]')
        search_input.fill("Playwright automation")
        page.keyboard.press("Enter")

        page.wait_for_selector("h3")

        page.locator("h3").first.click()

        page.wait_for_load_state("load")

        assert "Playwright" in page.title()

        browser.close()