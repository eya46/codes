from typing import List
from functools import cache


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def dfs(i) -> List[int]:
            floor = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    floor.append(1)
                else:
                    floor.append(dfs(i - 1)[j - 1] + dfs(i - 1)[j])
            return floor

        return dfs(rowIndex + 1)


if __name__ == "__main__":
    for i in range(5):
        print(i, Solution().getRow(i))
