class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]  # 오른쪽 값 추가

            while current_sum >= target:    # 왼쪽 줄여 최소길이 탐색
                min_len = min(min_len, right - left + 1)

                current_sum -= nums[left]   # 왼쪽 값 빼기
                left += 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len