# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1, tree2):   # 두 트리가 같은지 확인
            if tree1 is None and tree2 is None: # 같은 위치에서 끝났으므로 동일
                return True

            if tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False

            return(
                isSameTree(tree1.left, tree2.left)
                and isSameTree(tree1.right, tree2.right)
            )   # 왼쪽 서브트리와 오른쪽 서브트리가 동일해야 함

        if root is None:
            return False

        if isSameTree(root, subRoot):
            return True

        return(
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )