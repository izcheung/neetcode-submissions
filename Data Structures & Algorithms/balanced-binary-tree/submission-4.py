# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def maxDepth(root):
            if not root:
                return 0
            
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)
        
        maxDepth(root)
        return self.balanced



            
        