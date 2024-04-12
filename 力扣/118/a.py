from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(1, numRows + 1):
            floor = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    floor.append(1)
                    continue
                floor.append(res[i - 2][j - 1] + res[i - 2][j])
            res.append(floor)

        return res


if __name__ == "__main__":
    print(Solution().generate(5))
