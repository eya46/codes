from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for a, i in enumerate(numbers[:-1]):
            for b, j in enumerate(numbers[a + 1 :]):
                if i + j == target:
                    return [a + 1, b + a + 2]


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
