class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: # target을 찾은 경우
                return mid

            elif nums[mid] < target:    # target이 중간값보다 큼 -> 오른쪽 탐색
                left = mid + 1

            else:   # 왼쪽 탐색
                right = mid - 1

        return -1   # 끝까지 찾지 못한 경우