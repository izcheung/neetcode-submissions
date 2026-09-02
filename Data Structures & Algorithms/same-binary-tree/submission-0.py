# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base
        if (p and not q) or (q and not p):
            return False
        if not p and not q: #leaves
            return True
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left) # t/f
        right = self.isSameTree(p.right, q.right) # t/f

        return left and right #we need both to be true

        