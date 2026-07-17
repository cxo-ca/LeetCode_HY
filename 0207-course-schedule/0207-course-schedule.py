from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] # 각 과목을 이수한 뒤 들을 수 있는 다음 과목 저장
        indegree = [0]*numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque() # 선수 과목이 없는 과목부터
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0

        while queue:
            current = queue.popleft()   # 현재 바로 이수할 수 있는 과목 꺼냄
            completed += 1

            for next_course in graph[current]:  # 현재 과목을 선수 과목으로 가지는 다음 과목들 확인
                indegree[next_course] -= 1  # 현재 과목 이수했으므로 -1

                if indegree[next_course] == 0:   # 선수 과목을 모두 이수했으면 큐에 넣음
                    queue.append(next_course)

        return completed == numCourses  # 모든 과목 이수 시 순환구조 없으므로 True

