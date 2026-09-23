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
        def traverse(root, maxi):
            if not root:
                return 0
            goodNode = 0
            if root.val >= maxi:
                maxi = root.val #2
                goodNode += 1 #2
            left = traverse(root.left, maxi)
            right = traverse(root.right, maxi)
            return goodNode + left + right
        return traverse(root, root.val)
