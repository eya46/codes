from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
        while 1:
            s = numbers[a] + numbers[b]
            if s == target:
                return [a + 1, b + 1]
            if s > target:
                b -= 1
            else:
                a += 1


if __name__ == "__main__":
    print(
        Solution().twoSum([2, 7, 11, 15], 9)
    )
