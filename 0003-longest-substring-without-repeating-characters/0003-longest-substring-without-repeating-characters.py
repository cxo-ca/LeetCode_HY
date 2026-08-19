class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()   # 현재 구간에 들어있는 문자들
        left = 0
        max_len = 0

        for right in range(len(s)): # 현재 문자가 이미 구간 안에 있다면
            while s[right] in chars:    # 중복이 없어질때까지 왼쪽 줄임
                chars.remove(s[left])
                left += 1

            chars.add(s[right]) # 현재 문자를 구간에 추가

            max_len = max(max_len, right - left + 1)    # 현재 구간 길이

        return max_len