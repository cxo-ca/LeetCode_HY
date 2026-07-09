from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()    # 지금까지 나온 수들을 저장할 집합

        for num in nums:
            if num in seen: # 이미 나온 숫자가 또 나올 시
                return True # 중복이 있으므로 True 반환
            seen.add(num)   # 처음 나온 숫자는 seen에 저장

        return False    # 중복이 나오지 않으면 False 반환