# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I have to pass down the max and min
        # the root.val will be the max for left subtree
        # the root.val will be the min for right subtree
        # if root.val at anypoint doesn't fit within these two conditons, return false
        # at the end return true

        def traverse(root, mini, maxi):
            if not root:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            left = traverse(root.left, mini, root.val) # (2,mini,1)
            right = traverse(root.right, root.val, maxi) # (3,1,maxi)
            return left and right
        
        return traverse(root, float('-inf'), float('inf'))