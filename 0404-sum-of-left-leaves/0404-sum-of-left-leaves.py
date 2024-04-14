# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        Sum = 0
        if root.left is not None and root.left.right is None and root.left.left is None:
            Sum += root.left.val
        Sum += self.sumOfLeftLeaves(root.left)
        Sum += self.sumOfLeftLeaves(root.right)
        return Sum
        