# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for each node, if the node is equal or greater than the max then we can increment the number of good node
        # Pass down the number
        count = [0]
        def traverse(root, maxi):
            nonlocal count
            if not root:
                return 0

            if root.val >= maxi:
                maxi = root.val #2
                count[0] += 1 #2
            traverse(root.left, maxi)
            traverse(root.right, maxi)
            
        traverse(root, root.val)
        return count[0]
