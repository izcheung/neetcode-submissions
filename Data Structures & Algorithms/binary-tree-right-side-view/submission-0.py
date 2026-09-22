# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS, the last node
        ans = []
        if not root:
            return ans
        queue = deque([root])

        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level)
        
        final = []
        for each in ans:
            final.append(each[-1])
        return final


