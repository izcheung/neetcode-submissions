# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: #has subroot
            return False
        if self.isSametree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right


    
    def isSametree(self, p, q):
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val != q.val:
            return False
        left = self.isSametree(p.left, q.left)
        right = self.isSametree(p.right, q.right)
        return left and right