from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict

        d = defaultdict(list)
        for _, __ in edges:
            d[_].append(__)
            d[__].append(_)
        visit = set()

        def dfs(res):
            if res == destination:
                return True
            visit.add(res)
            for i in d[res]:
                if i not in visit and dfs(i):
                    return True
            return False

        return dfs(source)


if __name__ == "__main__":
    print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
