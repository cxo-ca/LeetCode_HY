# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False    # 현재 노드가 없다면 경로도 없음

        targetSum -= root.val    # 목표합에서 현재노드값 빼줌

        if root.left is None and root.right is None:
            return targetSum == 0   # 현재노드가 리프노드라면 목표합 0

        return(self.hasPathSum(root.left, targetSum)
                or self.hasPathSum(root.right, targetSum))  # 왼쪽 또는 오른쪽 자식에서 조건 만족하는 경로가 존재 시 True 반환