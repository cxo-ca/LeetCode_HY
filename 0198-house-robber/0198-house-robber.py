class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)    # dp[i]: 0~i번째 집까지 고려했을때 훔칠 수 있는 최대 금액

        dp[0] = nums[0] # 첫번째 집만 고려
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # 점화식 dp[i - 1] + dp[i - 2] + nums[i]

        return dp[-1]