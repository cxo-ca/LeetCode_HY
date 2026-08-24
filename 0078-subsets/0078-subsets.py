class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # 모든 부분집합 저장할 리스트
        subset = []  # 현재 만드는 부분집합

        def backtrack(start):   # 현재 상태도 하나의 부분집합 -> 저장
            result.append(subset[:])

            # start부터 뒤의 숫자들을 하나씩 선택
            for i in range(start, len(nums)):
                subset.append(nums[i])      # nums[i] 선택
                backtrack(i + 1)            # 다음 숫자 선택 위해 이동
                subset.pop()                # 백트래킹

        backtrack(0)

        return result