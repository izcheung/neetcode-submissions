# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - root, left, right
        # inorder - left, root, right

        if not preorder or not inorder:
            return None
    
        root = preorder[0]
        middle = inorder.index(root)

        leftArray = inorder[:middle]
        rightArray = inorder[middle+1:]

        rootNode = TreeNode(root)
        left = self.buildTree(preorder[1:middle + 1], leftArray)
        right = self.buildTree(preorder[middle+1:], rightArray)

        rootNode.left = left
        rootNode.right = right

        return rootNode




        