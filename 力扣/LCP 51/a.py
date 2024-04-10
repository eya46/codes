from typing import List


class Solution:
    def perfectMenu(
            self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int
    ) -> int:
        n = len(cookbooks)
        res = [-1]
        path = []

        def dfs(i):
            # 检查当前料理需求是否超过食材数量
            for left, use in zip(materials, [sum(__) for __ in zip(*[cookbooks[_] for _ in path])]):
                if use > left:
                    return

            # 检查是否满足饱腹感, 满足则添加
            if len(path) > 0 and sum(attribute[_][1] for _ in path) >= limit:
                res.append(sum(attribute[_][0] for _ in path))

            # 没得选了
            if i + 1 > n:
                return

            # 选i下标的料理
            path.append(i)
            dfs(i + 1)
            path.pop()

            # 不选i下标的料理
            dfs(i + 1)

        dfs(0)

        return max(res)


if __name__ == "__main__":
    print(Solution().perfectMenu(
        [4, 20, 16, 17, 14],
        [[3, 1, 6, 12, 18], [12, 7, 17, 19, 16], [18, 4, 7, 8, 0], [18, 9, 20, 16, 4], [17, 15, 4, 7, 15],
         [2, 8, 9, 3, 13], [20, 12, 0, 7, 17], [3, 2, 7, 5, 5]],
        [[13, 4], [7, 18], [3, 11], [6, 20], [9, 0], [13, 16], [18, 3], [2, 5]],
        1
    ))
