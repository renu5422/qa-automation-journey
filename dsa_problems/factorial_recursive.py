def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(0) == 1
    print(factorial(5))
