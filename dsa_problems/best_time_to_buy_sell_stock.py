def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1, 2, 3, 4, 5]) == 4

    print("All assertions passed.")
    print("Example: max_profit([7, 1, 5, 3, 6, 4]) ->", max_profit([7, 1, 5, 3, 6, 4]))