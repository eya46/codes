from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        res = []
        path = [2] * n

        def dfs(i):

            nonlocal path
            if i == n:
                return res.append(path.count(1))

            if path[i] == 1:  # 好人
                for idx, j in enumerate(statements[i]):
                    if j == 2:  # i未陈述
                        continue
                    if path[idx] == 2:  # j未确认身份
                        path[idx] = j
                    else:
                        if path[idx] != j:  # 已确认的身份和i说的不符, 认为是i有问题, 直接不考虑
                            return
                dfs(i + 1)
            elif path[i] == 2:  # 不确定
                # 坏人
                raw_path = path[:]
                path[i] = 0
                dfs(i + 1)
                path = raw_path
                # 好人
                path[i] = 1
                dfs(i)
            else:  # 坏人
                dfs(i + 1)

        dfs(0)

        return max(res)


if __name__ == "__main__":
    print(Solution().maximumGood([[2, 1, 2], [1, 2, 2], [2, 0, 2]]))
    print(Solution().maximumGood([[2, 0], [0, 2]]))
