class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(houses):
            prev2 = 0   # 두집 전까지의 최대 금액
            prev1 = 0   # 한집 전까지의 최대 금액

            for money in houses:
                current = max(prev2 + money, prev1)

                prev2 = prev1
                prev1 = current # 값 갱신
            
            return prev1

        case1 = rob_line(nums[:-1]) # 첫번째 집부터 마지막 전 집까지
        case2 = rob_line(nums[1:])  # 두번째 집부터 마지막 집까지

        return max(case1, case2)