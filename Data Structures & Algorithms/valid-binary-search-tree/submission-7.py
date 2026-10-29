# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, miniBoundary, maxiBoundary):
            if not root:
                return True
            if root.val <= miniBoundary:
                return False
            if root.val >= maxiBoundary:
                return False
            
            left = dfs(root.left, miniBoundary, root.val)
            right = dfs(root.right, root.val, maxiBoundary)

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))