class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):    # 0 ~ numRows - 1번째 줄까지 생성
            row = [1] * (i + 1) # i번째 줄에는 i + 1개의 숫자가 들어감, 각 줄의 양 끝은 항상 1

            for j in range(1, i):   # 양 끝을 제외한 가운데 숫자들을 계산
                row[j] = (
                    triangle[i - 1][j - 1]  # 바로 위 왼쪽 숫자
                    + triangle[i - 1][j]    # 바로 위 오른쪽 숫자
                )
            triangle.append(row)
        return triangle