class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):   # 2행부터 차례대로
            for j in range(i - 1, 0, -1):   # 오른쪽에서 왼쪽으로 갱신
                dp[j] = dp[j - 1] + dp[j]

        return dp