# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breadth first search since its going by levels instead of going one route furthest down (which would be dfs)
        # to implement bfs, use a queue
        ans = []
        # edge case
        if not root:
            return ans
        
        # initialize the queue with the root
     
        queue = deque([root])

        while queue: #[2, 3]
            currLevel = []
            queueLength = len(queue)
            for i in range(queueLength):
                current = queue.popleft()
                currLevel.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(currLevel)
        # [[1], ]
        return ans
            




