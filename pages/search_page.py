from utils.wait_helpers import safe_fill
class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.get_by_placeholder("Search")
        self.results = page.locator("h2")

    def goto(self):
        self.page.goto("https://duckduckgo.com/")

    def search(self, query):
        safe_fill(self.search_input, query, "Search Input")
        self.page.keyboard.press("Enter")

    def wait_for_results(self):
        self.results.first.wait_for(timeout=10000)

    def get_results_count(self):
        return self.results.count()

    def is_results_loaded(self):
        return self.results.count() > 0

    def click_first_result(self):
        self.results.first.click()

    def wait_for_page_title(self, title_text):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_function(
            f"document.title.includes('{title_text}')",
            timeout=5000
        )

    def search_and_wait(self, query):
        self.goto()
        self.search(query)
        self.wait_for_results()