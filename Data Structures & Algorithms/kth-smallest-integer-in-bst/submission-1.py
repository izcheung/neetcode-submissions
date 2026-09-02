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
        # def traverse(root, curr, k):
        #     if not root:
        #         return 0
        #     left = traverse(root.left, curr + 1, k)
        #     if curr == k:
        #         return root.val
        #     right = traverse(root.right, curr + 1, k)
            
        
        # curr = 0
        # return traverse(root, curr, k)
        ans = []
        def traverse(root):
            if not root:
                return
            left = traverse(root.left)
            ans.append(root.val)
            right = traverse(root.right)
            
            return ans


        traverse(root)
        return ans[k-1]

