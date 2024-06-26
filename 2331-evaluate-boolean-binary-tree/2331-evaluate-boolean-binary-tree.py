# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        l1 = self.evaluateTree(root.left)
        r1 = self.evaluateTree(root.right)
        if root.val == 3:
            return l1 and r1
        return l1 or r1