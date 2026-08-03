class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1) # ans[i]: 숫자 i를 이진수로 표현했을 때 1의 개수

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # ans[i >> 1]: 몫, (i & 1): i가 홀수면 1, 짝수면 0

        return ans