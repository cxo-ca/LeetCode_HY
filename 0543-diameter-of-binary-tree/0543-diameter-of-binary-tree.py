# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def get_depth(node):
            if node is None:
                return 0    # 노드가 없으면 깊이는 0

            left_depth = get_depth(node.left)   # 왼쪽 서브트리의 최대 깊이
            right_depth = get_depth(node.right) # 오른쪽 서브트리의 최대 깊이

            self.diameter = max(self.diameter, left_depth+right_depth)

            return max(left_depth,right_depth)+1

        get_depth(root) # 루트부터 모든 노드의 깊이 계산

        return self.diameter    # 최종적으로 가장 긴 것 반환