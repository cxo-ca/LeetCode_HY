from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False]*n

        province_count = 0

        for city in range(n):   # 모든 도시 차례대로 확인
            if visited[city]:   # 같은 province
                continue
            province_count += 1 # 다른 province
            queue = deque([city])
            visited[city] = True

            while queue:    # 현재 도시와 연결된 모든 도시 탐색
                current = queue.popleft()

                for next_city in range(n):
                    # 연결되어있고 아직 방문하지 않은 경우
                    if(
                        isConnected[current][next_city] == 1
                        and not visited[next_city]
                    ):
                        visited[next_city] = True
                        queue.append(next_city)

        return province_count