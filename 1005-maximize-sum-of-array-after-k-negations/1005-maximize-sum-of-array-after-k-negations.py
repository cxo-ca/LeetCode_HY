class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort() # 오름차순

        for i in range (len(nums)):
            if nums[i] < 0 and k > 0:   # 현재 값이 음수고 더 뒤집을 수 있을 때
                nums[i] = -nums[i]  # 음수 -> 양수
                k -= 1

        total = sum(nums)

        if k % 2 == 1:  # k가 홀수
            total -= 2 * min(nums)  # x -> -x

        return total