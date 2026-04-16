from playwright.sync_api import Page

from config.settings import BASE_URL
from utils.helpers import HelperUtils


class SearchPage:
    URL = BASE_URL

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('input[name="q"]')
        self.results = page.locator("h2")

    def open(self) -> None:
        self.page.goto(self.URL)

    def search(self, text: str) -> None:
        self.search_input.fill(text)
        self.page.keyboard.press("Enter")

    def get_results_count(self) -> int:
        HelperUtils.wait_for_element(self.results.first)
        return self.results.count()
