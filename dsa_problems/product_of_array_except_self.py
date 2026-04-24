def product_except_self(nums):
    n = len(nums)

    result = [1] * n

    # Prefix products
    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Postfix products
    postfix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


# =========================
# TEST CASES
# =========================

assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

assert product_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]

assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


print("All test cases passed!")