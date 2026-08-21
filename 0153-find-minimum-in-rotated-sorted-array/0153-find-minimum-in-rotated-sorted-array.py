class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right: # 최솟값 있는 위치 이진탐색
            mid = (left + right) // 2

            if nums[mid] > nums[right]: # mid값이 오른쪽끝값보다 큼 -> 최솟값은 mid 오른쪽에
                left = mid + 1
            else:   # # mid값이 오른쪽끝값보다 작음 -> 최솟값은 mid or mid 왼쪽에
                right = mid

        return nums[left]