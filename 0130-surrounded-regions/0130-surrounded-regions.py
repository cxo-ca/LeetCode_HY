from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        if not board or not board[0]:
            return  # 보드가 비어있으면 종료

        m = len(board)
        n = len(board[0])   # 행과 열

        queue = deque() # BFS

        # 상 하 좌 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def save(x:int, y:int) -> None:
            if board[x][y] != "O":
                return
            board[x][y] = "S"
            queue.append((x, y))

        for x in range(m):  # 왼쪽, 오른쪽 테두리 확인
            save(x, 0)
            save(x, n-1)

        for y in range(n):   # 위쪽, 아래쪽 테두리 확인
            save(0, y)
            save(m-1, y)

        while queue:
            x, y = queue.popleft()
            for i in range(4):  # 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n: # 보드 내부인지 확인
                    if board[nx][ny] == "O":
                        board[nx][ny] = "S"
                        queue.append((nx, ny))

        for x in range(m):  # 최종 변환
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "S":
                    board[x][y] = "O"