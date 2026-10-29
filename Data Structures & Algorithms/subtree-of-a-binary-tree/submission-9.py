# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Traverse down root, and check if it is the same tree as subroot

        def sameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if (p.val != q.val):
                return False

            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)

            return left and right
        
        if not subRoot:
            return True
        if not root:
            return False
        
        curr = sameTree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
    
        return curr or left or right 