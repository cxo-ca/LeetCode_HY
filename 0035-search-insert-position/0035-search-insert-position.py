class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1    # 탐색 범위 설정

        while left <= right:    # 범위가 남아있는동안 반복
            mid = (left + right) // 2

            if nums[mid] == target: # target 발견
                return mid
            elif nums[mid] < target:    # 중간값보다 target이 큼 -> 오른쪽 절반 탐색
                left = mid + 1
            else:   # 중간값보다 target이 작음 -> 왼쪽 절반 탐색
                right = mid - 1

        return left