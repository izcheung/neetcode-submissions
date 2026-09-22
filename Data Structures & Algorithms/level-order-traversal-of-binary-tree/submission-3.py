# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue BFS traversal
        # left to right
        '''
        q = [2, 3]
        level = [1]
        length = 1
        curr = 1
        ans = [[1],]
        '''
        ans = []
        if not root:
            return ans

        queue = deque()
        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level)
        return ans
                
