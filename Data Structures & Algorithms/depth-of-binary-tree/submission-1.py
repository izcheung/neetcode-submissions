# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # each node = 1
        left = self.maxDepth(root.left) #1
        right = self.maxDepth(root.right) #2

        return 1 + max(left, right) # 3