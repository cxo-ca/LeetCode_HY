# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:    # 노드가 없다면 깊이는 0
            return 0

        left_depth = self.maxDepth(root.left) # 왼쪽 서브트리의 최대 깊이를 재귀적으로 계산

        right_depth = self.maxDepth(root.right) # 오른쪽 서브트리의 최대 깊이를 재귀적으로 계산

        return max(left_depth, right_depth)+1