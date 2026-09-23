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
        self.count = 0
        
        def traverseBST(root):
            if not root:
                return None

            left = traverseBST(root.left)

            self.count += 1
            if self.count == k:
                return root.val
                
            right = traverseBST(root.right)

            if left is not None:
                return left

            if right is not None:
                return right

        
        return traverseBST(root)


