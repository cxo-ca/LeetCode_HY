class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(start, total, path):
            if total == target: # 합이 target과 같음 -> 정답에 추가
                answer.append(path[:])
                return

            if total > target:  # target 넘어감 -> 탐색할 필요x
                return

            for i in range(start, len(candidates)): # 중복 조합 방지
                path.append(candidates[i])

                backtrack(i, total+candidates[i], path)

                path.pop()

        backtrack(0, 0, [])

        return answer