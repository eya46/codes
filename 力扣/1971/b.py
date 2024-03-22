from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for u, v in edges:
            p[find(u)] = find(v)
        return find(source) == find(destination)


if __name__ == "__main__":
    print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
