class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # 완성된 순열 저장할 리스트

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])  # 현재 path 복사하여 저장
                return

            for num in nums:    # 숫자를 하나씩 확인
                if num in path: # 이미 사용한 숫자 -> 건너뛰기
                    continue

                path.append(num)    # 숫자 선택
                backtrack(path) # 다른 숫자 선택하러 이동
                path.pop()  # 선택했던 숫자 삭제

        backtrack([])

        return result