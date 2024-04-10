from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        # 列数
        n = len(matrix[0])

        res = []
        # 当前选择的列
        path = []

        def dfs(i):

            # 选完了
            if len(path) == numSelect:
                return res.append(
                    len(list(  # 全为0的行的数量
                        filter(
                            lambda x: sum(x) == 0,  # 判断和为0
                            [
                                [col for idx, col in enumerate(row) if idx not in path]  # 筛去已经选择的列
                                for row in matrix  # 遍历行
                            ]
                        )
                    ))
                )

            # 超出矩阵没得选了
            if i > n - 1:
                return

            # 选择当前列
            path.append(i)
            dfs(i + 1)
            path.pop()

            # 不选当前列
            dfs(i + 1)

        dfs(0)

        return max(res)


if __name__ == "__main__":
    print(Solution().maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2))
