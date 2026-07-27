class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 올라가는 방법의 수
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):   # 3번째 계단부터
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]