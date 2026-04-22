# tests/test_search_edge_cases.py

import re
import pytest
from playwright.sync_api import expect
from pages.search_page import SearchPage


def test_empty_search(page):
    page.goto("https://duckduckgo.com/")

    page.keyboard.press("Enter")

    page.wait_for_load_state("load")

    assert "duckduckgo.com" in page.url, "Empty search caused unexpected behavior"
    assert len(page.title()) > 0, "Page did not load properly"


def test_long_search_input(page):
    page.goto("https://duckduckgo.com/")

    long_query = "a" * 500
    page.get_by_placeholder("Search").fill(long_query)

    page.keyboard.press("Enter")
    page.wait_for_load_state("load")

    assert "duckduckgo.com" in page.url, "Long input caused failure"


def test_special_character_search(page):
    page.goto("https://duckduckgo.com/")

    page.get_by_placeholder("Search").fill("#$%^&*()")

    page.keyboard.press("Enter")
    page.wait_for_load_state("load")

    assert "duckduckgo.com" in page.url, "Special character search failed"
    expect(page).not_to_have_title("", timeout=10000)


def test_unicode_search(page):
    page.goto("https://duckduckgo.com/")

    page.get_by_placeholder("Search").fill("தமிழ் மொழி")

    page.keyboard.press("Enter")
    page.wait_for_load_state("load")

    assert "duckduckgo.com" in page.url, "Unicode search failed"


def test_rapid_search(page):
    page.goto("https://duckduckgo.com/")

    search_input = page.get_by_placeholder("Search")

    search_input.fill("Playwright")
    page.keyboard.press("Enter")

    page.wait_for_load_state("load")
    page.locator('input[name="q"]').fill("Python")
    page.keyboard.press("Enter")

    page.wait_for_load_state("load")

    assert "duckduckgo.com" in page.url, "Rapid search caused instability"
def test_bang_redirect_behavior(page):
    page.goto("https://duckduckgo.com/")

    page.get_by_placeholder("Search").fill("!w python")
    page.keyboard.press("Enter")

    expect(page).to_have_url(re.compile("wikipedia.org"), timeout=30000)

    assert "wikipedia.org" in page.url, "Bang redirect did not work as expected"
def test_empty_search_pom(page):
    search_page = SearchPage(page)

    search_page.goto()
    search_page.search("")

    assert page.url != "", "Page should not crash on empty search"