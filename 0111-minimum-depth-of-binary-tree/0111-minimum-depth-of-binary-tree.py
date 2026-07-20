# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0    # 트리가 비어있다면 깊이는 0

        queue = deque([(root, 1)])    # (현재노드, 현재깊이)

        while queue:    # BFS
            node, depth = queue.popleft()

            if node.left is None and node.right is None:    # 리프노드
                return depth

            if node.left is not None:   # 왼쪽에 자식노드가 있다면 다음 깊이로 큐에 추가
                queue.append((node.left, depth+1))

            if node.right is not None:  # 오른쪽에 자식노드가 있다면 다음 깊이로 큐에 추가
                queue.append((node.right, depth+1))