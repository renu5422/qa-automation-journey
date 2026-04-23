"""Centralized test data and constants for QA automation framework."""

# =========================
# SEARCH TEST DATA
# =========================

SEARCH_QUERIES = {
    "basic": "Playwright automation",
    "long": "a" * 500,
    "special_chars": "#$%^&*()",
    "unicode": "தமிழ் மொழி",
    "wikipedia_bang": "!w python",
}

# =========================
# EDGE CASE INPUTS
# =========================

EDGE_CASES = {
    "empty_string": "",
    "whitespace_only": "   ",
    "very_long_input": "x" * 1000,
    "rapid_queries": [
        "Playwright",
        "Python",
        "Automation"
    ],
}

# =========================
# TEST URLS
# =========================

TEST_URLS = {
    "duckduckgo": "https://duckduckgo.com",
    "google": "https://www.google.com",
    "wikipedia": "https://wikipedia.org",
}

# =========================
# SELECTORS
# =========================

SELECTORS = {
    "duckduckgo_search_input": 'input[name="q"]',
    "duckduckgo_results": '[data-testid="result"]',
}

# =========================
# EXPECTED TEST VALUES
# =========================

EXPECTED_RESULTS = {
    "min_results": 1,
    "timeout_ms": 5000,
    "navigation_timeout_ms": 10000,
}