# QA Automation Journey

This repository contains Playwright + Pytest UI automation work and Python DSA practice.

## Current Status

- UI automation suite is passing: 12/12 tests.
- DSA folder has cleaned, descriptive filenames.
- Added `best_time_to_buy_sell_stock.py` with assertion-based checks.

## Project Structure

```text
qa-automation-journey/
├── config/
├── dsa_problems/
├── pages/
├── screenshots/
├── tests/
├── utils/
├── pyproject.toml
├── requirements.txt
├── README.md
└── test-results.txt
```

## Run Tests

```powershell
c:/Users/Admin/qa-automation-journey/.venv/Scripts/python.exe -m pytest tests/ -v --tb=short
```

## Latest UI Test Result

12 passed in 70.17s.

## DSA: Best Time to Buy and Sell Stock

File: `dsa_problems/best_time_to_buy_sell_stock.py`

### Problem
Given a list of prices where `prices[i]` is the stock price on day `i`, find the maximum profit from one buy and one sell. You must buy before you sell.

### Approach (One Pass)

Track two values while scanning left to right:

1. `min_price`: cheapest price seen so far.
2. `max_profit`: best profit seen so far.

For each price:

- Update `min_price` if current price is lower.
- Compute current profit as `price - min_price`.
- Update `max_profit` if this profit is better.

### Complexity

- Time: O(n)
- Space: O(1)

### Assertions Included

The script includes runtime assertions:

- `[7, 1, 5, 3, 6, 4] -> 5`
- `[7, 6, 4, 3, 1] -> 0`
- `[2, 4, 1] -> 2`
- `[1, 2, 3, 4, 5] -> 4`

Run it directly:

```powershell
c:/Users/Admin/qa-automation-journey/.venv/Scripts/python.exe dsa_problems/best_time_to_buy_sell_stock.py
```
