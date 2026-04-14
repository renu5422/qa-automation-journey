# QA Automation Journey

This repository tracks my learning journey into QA Automation using Python and Playwright.

---

## Today's Work

### QA Automation
- Added `pages/search_page.py` as a Page Object Model class.
- Added `tests/test_search_pom.py` to validate DuckDuckGo search with POM.
- Added `config/settings.py` and `conftest.py` for shared fixture support.
- Ran Playwright tests and saved the latest output to `test-results.txt`.

### DSA Practice
- Added and validated DSA scripts including anagram and duplicate detection problems.
- Added assertion checks in each DSA script so each program verifies correct output at runtime.
- Confirmed `Valid Anagram.py` returns `True` for `"listen"` and `"silent"`.
- Confirmed `validate duplicate.py` returns `True` for duplicate input `[1, 2, 3, 1]`.

---

## Daily Progress
- Day 1: Implemented reverse string logic and assertion verification.
- Day 2: Implemented palindrome validation with assertion examples.
- Day 3: Implemented vowel counting and assertion-based checks.
- Day 4: Implemented anagram comparison with assertions.
- Day 5: Implemented recursive factorial and runtime assertions.

---

## Project Structure
qa-automation-journey/
├── .github/                     # GitHub workflows / CI later
├── .venv/                       # Virtual environment
├── pages/                       # Page Object Model classes
│   └── search_page.py
├── tests/                       # Test cases only
│   ├── test_duckduckgo_search.py
│   ├── test_duckduckgo_navigation.py
│   ├── test_duckduckgo_results_count.py
│   ├── test_google.py
│   └── test_search_pom.py
├── dsa_problems/                # DSA practice
│   ├── dsa_day1.py
│   ├── dsa_day2.py
│   ├── dsa_day3.py
│   ├── dsa_day4.py
│   └── dsa_day5.py
├── utils/                       # Utility/helper methods (future)
│   └── helpers.py
├── config/                      # Config/constants (future)
│   └── settings.py
├── conftest.py                  # Shared pytest fixtures
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
└── test-results.txt

---

## How to Run Tests

```bash
pytest -q tests
```

---

## Notes
- `test-results.txt` contains the latest test output.
- Use the project virtual environment before running tests if available.
