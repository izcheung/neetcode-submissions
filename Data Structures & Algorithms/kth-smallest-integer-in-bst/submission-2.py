# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the binary tree, appendign the value in ascending order into an array, reutrn the kth smallest value (it is 1 insdex so + 1)
        # Traversal - left, root, right
        bst = []
        
        def traverseBST(root):
            if not root:
                return
            left = traverseBST(root.left)
            bst.append(root.val)
            right = traverseBST(root.right)
        
        traverseBST(root)
        return bst[k-1]