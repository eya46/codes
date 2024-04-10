from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        def dfs(i):
            if i == n:
                if len(path) > 0:
                    # res.append(list(filter(lambda x: x == x[::-1], path)))
                    res.append(path[:])
                return

            for j in range(i, n):
                data = s[i:j + 1]
                if data == data[::-1]:
                    path.append(data)
                    dfs(j + 1)
                    path.pop()

        dfs(0)

        return res


if __name__ == "__main__":
    print(Solution().partition("aab"))
