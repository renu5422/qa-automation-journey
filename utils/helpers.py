import os

from playwright.sync_api import Locator, Page


class HelperUtils:
    @staticmethod
    def take_screenshot(page: Page, file_name: str) -> None:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path=f"screenshots/{file_name}.png")

    @staticmethod
    def wait_for_element(locator: Locator) -> None:
        locator.wait_for(state="visible")
