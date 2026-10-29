# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # need to keep track of max
        def dfs(root, maxSoFar):
            if not root:
                return 0

            goodNode = 0

            if root.val >= maxSoFar:
                goodNode = 1
                goodNode += dfs(root.left, root.val)
                goodNode += dfs(root.right, root.val)
            else:
                goodNode += dfs(root.left, maxSoFar)
                goodNode += dfs(root.right, maxSoFar)
            
            return goodNode
        
        return dfs(root, root.val)

    

           