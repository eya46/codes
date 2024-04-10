from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = [0] * n
        select = [False] * n

        def dfs(i):
            if i == n:
                res.append(path[:])

            for j in range(n):
                if not select[j]:
                    path[i] = nums[j]
                    select[j] = True
                    dfs(i + 1)
                    select[j] = False

        dfs(0)

        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
