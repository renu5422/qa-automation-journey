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
        self.results.first.wait_for(timeout=5000)

    def get_results_count(self):
        return self.results.count()
    def is_results_loaded(self):
        return self.results.count() > 0