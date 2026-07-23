from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root.left, root.right)])    # 왼쪽자식 오른쪽자식 한 쌍으로 큐에 저장

        while queue:
            left, right = queue.popleft()   # 대칭위치에 있어야하는 두 노드 꺼냄

            if left is None and right is None:  # 해당하는 경우
                continue
            if left is None or right is None:   # 예외
                return False
            if left.val != right.val:   # 예외
                return False

            queue.append((left.left, right.right))    # 바깥쪽끼리 비교
            queue.append((left.right, right.left))    # 안쪽끼리 비교

        return True