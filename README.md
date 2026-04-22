# QA Automation Journey

This repository captures the QA automation learning journey using Python, Playwright, and data structure practice problems.

---

## What this repo contains
- A Playwright Page Object Model for DuckDuckGo search.
- Reusable helper utilities for screenshots, safe fill, and element waiting.
- Pytest-based regression and edge-case tests for search flows.
- DSA practice scripts for common algorithm problems.
- A running test result summary in `test-results.txt`.

---

## Current progress
### Day 9 summary
- Added `test_empty_search_pom` — verifies empty search via the `SearchPage` POM doesn't crash the page.
- Fixed `test_bang_redirect_behavior` — replaced unreliable `wait_for_url` with `expect(page).to_have_url(re.compile(...))` which polls the live URL and handles multi-hop redirects (DuckDuckGo → redirect intermediary → Wikipedia).
- Fixed duplicate `test_empty_search` naming conflict — renamed POM variant to `test_empty_search_pom`.
- All 13 tests passing across 6 test files.

### Day 8 summary
- Removed all `time.sleep()` calls — replaced with proper Playwright waits.
- Fixed locators: replaced weak `h2` selectors with `[data-testid="result"]` for stability.
- Added `test_search_edge_cases.py` with 6 edge-case tests covering empty input, long input, special characters, unicode, rapid search, and DuckDuckGo bang redirects.
- Fixed `test_long_search_input` in POM suite — asserts load and URL instead of waiting for results that never appear.
- Strengthened assertions with failure messages and `expect(page).not_to_have_title()` for navigation-safe title checks.
- All 12 tests passing.

### QA Automation work
- `SearchPage` POM with navigation, search, and results count methods.
- Centralized base URL and default search term in `config/settings.py`.
- `HelperUtils` in `utils/helpers.py` for safe fill, safe click, safe wait, and screenshots.
- Edge-case coverage: empty search, 500-char input, special characters, unicode, rapid sequential search, bang redirect behavior.
- Locators use `[data-testid="result"]`, `input[name="q"]`, and `get_by_placeholder("Search")` — no positional or index-based selectors.

### DSA practice work
- Implemented `dsa_6_longest_common_prefix.py` and `dsa_6_valid_palindrome.py`.
- Implemented Two Sum using a hashmap (O(n) time, O(n) space).
- Assertion-based examples in all DSA scripts for quick verification.

---

## DSA deep dive — Two Sum (hashmap approach)

### Problem
Given a list of numbers and a target, return the indices of the two numbers that add up to the target.

### Brute force vs hashmap

**Brute force** checks every pair — O(n²) time:
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Hashmap** does it in a single pass — O(n) time:
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```

### Why the hashmap works

For each number, instead of searching forward for its complement, you ask:
> "Has the number I need already gone past me?"

The `seen` dict stores every number encountered so far, mapped to its index.

Step-by-step with `[2, 7, 11, 15]`, target `9`:

| Step | `num` | `diff = 9 - num` | `seen` before check | Match? |
|------|-------|-------------------|----------------------|--------|
| 0 | 2 | 7 | `{}` | No → store `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | **Yes** → return `[0, 1]` |

The key insight: `diff in seen` is O(1) — dictionary lookups in Python are constant time because they use a hash table internally. This turns a nested loop into a single pass.

### Complexity
| | Brute force | Hashmap |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(n) |

### Test results
```
two_sum([2, 7, 11, 15], 9)  → [0, 1]  ✓
two_sum([3, 2, 4], 6)       → [1, 2]  ✓
two_sum([3, 3], 6)           → [0, 1]  ✓
two_sum([1, 2, 3], 100)      → []      ✓
```

---

## Project structure

```text
qa-automation-journey/
├── config/                        # Shared configuration values
│   └── settings.py                # BASE_URL, DEFAULT_SEARCH_TERM
├── dsa_problems/                  # Algorithm practice scripts
│   ├── dsa_6_longest_common_prefix.py
│   ├── dsa_6_valid_palindrome.py
│   ├── dsa_5.py  →  dsa.py
│   ├── dsa_day1.py  →  dsa_day5.py
│   ├── python_basics.py
│   ├── Valid Anagram.py
│   └── validate duplicate.py
├── pages/                         # Page Object Model classes
│   └── search_page.py             # SearchPage (open, search, get_results_count)
├── screenshots/                   # Captured screenshots on test run
├── tests/                         # Pytest test cases
│   ├── conftest.py                # page fixture (pytest-playwright)
│   ├── test_google.py             # Sanity: Google title check
│   ├── test_duckduckgo_search.py  # Core search + result visibility
│   ├── test_navigation.py         # Click result and verify navigation
│   ├── test_results_count.py      # Assert >= 5 results returned
│   ├── test_search_pom.py         # POM-based search, empty, and long input tests
│   └── test_search_edge_cases.py  # Edge cases: empty, long, special chars, unicode, rapid, bang
├── utils/                         # Utility modules
│   └── helpers.py                 # HelperUtils: safe_fill, safe_click, safe_wait, take_screenshot
├── conftest.py                    # Shared fixtures (base_url)
├── pyproject.toml                 # Python project configuration
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
└── test-results.txt               # Latest test output
```

---

## How to run tests

Activate the virtual environment first:

```powershell
cd C:\Users\Admin\qa-automation-journey
.venv\Scripts\Activate.ps1
```

Run all tests:

```powershell
pytest tests/ -v
```

Run a specific file:

```powershell
pytest tests/test_search_edge_cases.py -v
```

Run a single test:

```powershell
pytest tests/test_search_edge_cases.py::test_special_character_search -v
```

---

## Test suite overview

| File | Tests | Description |
|---|---|---|
| `test_google.py` | 1 | Google page title sanity check |
| `test_duckduckgo_search.py` | 1 | Search and assert result visible |
| `test_navigation.py` | 1 | Search → click result → verify navigation |
| `test_results_count.py` | 1 | Assert >= 5 results returned |
| `test_search_pom.py` | 3 | POM-based: normal search, empty input, long input |
| `test_search_edge_cases.py` | 6 | Empty, long, special chars, unicode, rapid, bang redirect |
| **Total** | **13** | **All passing** |

---

## Latest test status
All 12 tests pass as of Day 8. Run `pytest tests/ -v` for live results.

---

## Known gotchas

### DuckDuckGo bang syntax
DuckDuckGo supports "bang" shortcuts that redirect to external sites. For example, `!@` redirects to Twitter and `!w` redirects to Wikipedia. Using `!` at the start of a search query in tests will cause unexpected redirects away from `duckduckgo.com`, breaking URL assertions.

`test_special_character_search` uses `#$%^&*()` instead of `!@#$%^&*()` to avoid triggering a bang redirect.

`test_bang_redirect_behavior` intentionally tests this behavior by searching `!w python` and asserting the redirect lands on `wikipedia.org`.


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
