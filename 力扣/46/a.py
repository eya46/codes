from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
