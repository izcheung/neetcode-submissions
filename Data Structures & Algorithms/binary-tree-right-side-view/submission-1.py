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
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if i == length-1:
                    ans.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return ans


