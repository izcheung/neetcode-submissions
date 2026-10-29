# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.goodNodeCount = 0

        def dfs(root, maxSoFar):
            if not root:
                return

            if root.val >= maxSoFar:
                self.goodNodeCount += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, maxSoFar)
                dfs(root.right, maxSoFar)
            
        
        dfs(root, root.val)
        return self.goodNodeCount

    

           