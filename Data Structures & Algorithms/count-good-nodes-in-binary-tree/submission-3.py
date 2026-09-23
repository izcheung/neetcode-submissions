# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNode = 0
        
        def traverse(root, maxi):
            if not root:
                return 0
         
            if root.val >= maxi:
                maxi = root.val
                self.goodNode += 1
            left = traverse(root.left, maxi)
            right = traverse(root.right, maxi)

        traverse(root, root.val)
        return self.goodNode