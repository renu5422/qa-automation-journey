# QA Automation Journey

This repository captures the QA automation learning journey using Python, Playwright, and data structure practice problems.

---

## What this repo contains
- A Playwright Page Object Model for DuckDuckGo search.
- Reusable helper utilities for screenshots and element waiting.
- Pytest-based regression tests for search flows.
- DSA practice scripts for common algorithm problems.
- A running test result summary in `test-results.txt`.

---

## Current progress
### Day 7 summary
- Refactored `pages/search_page.py` to use a class-level `URL` constant.
- Moved default app values into `config/settings.py`.
- Updated `tests/test_search_pom.py` to use `DEFAULT_SEARCH_TERM`.
- Added screenshot capture after the POM search flow.
- Renamed DuckDuckGo test files for better organization.
- Documented this progress in the README.

### QA Automation work
- Created a reusable `SearchPage` object with navigation, search, and results count methods.
- Centralized base URL and default search term in `config/settings.py`.
- Added a helper class in `utils/helpers.py` for screenshots and element waiting.
- Kept the test flow simple and maintainable.

### DSA practice work
- Implemented `dsa_problems/dsa_6_longest_common_prefix.py`.
- Implemented `dsa_problems/dsa_6_valid_palindrome.py`.
- Kept assertion-based examples in DSA scripts for quick verification.

---

## Project structure

```text
qa-automation-journey/
├── config/                  # Shared configuration values
│   └── settings.py
├── dsa_problems/            # Algorithm practice scripts
│   ├── dsa_6_longest_common_prefix.py
│   ├── dsa_6_valid_palindrome.py
│   ├── dsa_5.py
│   ├── dsa_4.py
│   ├── dsa_3.py
│   ├── dsa_2.py
│   ├── dsa.py
│   ├── dsa_day1.py
│   ├── dsa_day2.py
│   ├── dsa_day3.py
│   ├── dsa_day4.py
│   ├── dsa_day5.py
│   ├── python_basics.py
│   ├── "Valid Anagram.py"
│   └── "validate duplicate.py"
├── pages/                   # Page object classes
│   └── search_page.py
├── tests/                   # Pytest test cases
│   ├── conftest.py
│   ├── test_google.py
│   ├── test_search_pom.py
│   ├── test_navigation.py
│   ├── test_results_count.py
│   ├── test_duckduckgo_search.py
│   └── test_duckduckgo_search.py
├── utils/                   # Utility modules
│   └── helpers.py
├── conftest.py              # Shared pytest fixtures
├── pyproject.toml           # Python project configuration
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── test-results.txt         # Latest test output
```

---

## How to run tests

Use the virtual environment Python interpreter:

```powershell
cd c:\Users\Admin\qa-automation-journey
.\.venv\Scripts\python.exe -m pytest tests/test_search_pom.py -q
```

Or run all tests:

```powershell
.\.venv\Scripts\python.exe -m pytest tests -q
```

---

## Latest test status
- `test-results.txt` currently records: `1 passed in 31.58s`.

---

## Notes for next steps
- Add more Page Object Model tests for navigation and result count.
- Add a Playwright fixture for browser options if needed.
- Continue DSA practice with additional algorithm problems.

---

## How to contribute / extend this repo
- Add new DSA practice scripts under `dsa_problems/` and include runtime assertions in `if __name__ == "__main__"` blocks.
- Add new Page Object Model classes under `pages/`, keeping element locators and actions encapsulated.
- Add new regression tests under `tests/` and reuse shared fixtures from `conftest.py`.
- Keep shared values like base URLs and default search terms in `config/settings.py`.
- Run `.\.venv\Scripts\python.exe -m pytest tests -q` after changes and update `test-results.txt`.
- Update this `README.md` with a new day summary and status whenever you add work.
