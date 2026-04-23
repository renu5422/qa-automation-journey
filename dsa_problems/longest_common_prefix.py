from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    examples = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interview", "internet", "internal"], "inte"),
    ]

    for strs, expected in examples:
        result = longest_common_prefix(strs)
        print(f"Input: {strs}")
        print(f"Output: {result}")
        assert result == expected
    print("All tests passed.")