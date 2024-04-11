from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """j<i,nums[j]<nums[i]"""
        """dfs(i)=max(dfs(j))+1"""
        """f[i]=max(f[j])+1"""
        n = len(nums)
        f = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j])
            f[i] += 1

        return max(f)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([7, 7, 7, 7]))
