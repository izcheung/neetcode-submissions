# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, maxi, mini):
            # base case
            if not root:
                return True

            # current node
            if root.val >= maxi or root.val <= mini:
                return False
            # if root.left and root.left.val >= root.val or root.left.val > maxi:
            #     return False
            # if root.right and root.right.val <= root.val or root.right.val < mini:
            #     return False

            left = check(root.left, root.val, mini)
            right = check(root.right, maxi, root.val)
            return left and right

        maxi = float('inf')
        mini = float('-inf')

        return check(root, maxi, mini)