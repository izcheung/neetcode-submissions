# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0
        def maxHeight(root):
            if not root:
                return 0
            left = maxHeight(root.left)
            right = maxHeight(root.right)
            self.maxDia = max(self.maxDia, left + right)
            return 1 + max(left, right)
        maxHeight(root)
        return self.maxDia