from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('input[name="q"]')
        self.results = page.locator("h2")

    def open(self) -> None:
        self.page.goto("https://duckduckgo.com")

    def search(self, text: str) -> None:
        self.search_input.fill(text)
        self.page.keyboard.press("Enter")

    def get_results_count(self) -> int:
        self.page.wait_for_selector("h2")
        return self.results.count()
