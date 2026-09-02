# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return 1 + max(left, right)
        