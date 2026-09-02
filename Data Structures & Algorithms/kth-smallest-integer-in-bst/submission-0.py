# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Its a binary search tree, left is smaller than root, right is greater than root
        # traverse through the binary search tree, and save the values in an array in order from least to greatest, then return the k-1th place
        def traverse(root, ans):
            if not root:
                return
            left = traverse(root.left, ans)
            ans.append(root.val)
            right = traverse(root.right, ans)
            
            return ans

        ans = []
        traverse(root, ans)
        return ans[k-1]
