from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = [0] * n

        def dfs(i, s):
            if i == n:
                res.append(path[:])

            for j in s:
                path[i] = j
                dfs(i + 1, s - {j})

        dfs(0, set(nums))

        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
