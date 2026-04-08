from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )
        page = context.new_page()

        page.goto("https://www.google.com")

        search_input = page.locator('textarea[name="q"]')
        search_input.wait_for(state="visible", timeout=10000)

        assert search_input.is_visible()
        context.close()
        browser.close()