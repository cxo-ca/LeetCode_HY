# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:    # 트리가 비어있으면 빈 리스트 반환
            return []

        result = [] # 최종결과 저장할 리스트

        queue = deque([root]) # 방문할 노드를 저장, 처음에는 루트노드

        while queue:    # 방문할 노드가 남아있을 때까지 반복
            level_size = len(queue) # 현재 층에 있는 노드의 개수 저장
            current_level = []  # 현재 층의 노드 값 저장

            for _ in range(level_size): # 현재 층의 노드 개수만큼 반복
                node = queue.popleft() # 맨앞 노드를 꺼냄
                current_level.append(node.val)  # 꺼낸 노드의 값을 현재 층 리스트에 추가

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(current_level)    # 현재 층 탐색 종료 -> 결과에 추가
        
        return result
