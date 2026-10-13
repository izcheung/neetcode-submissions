"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def dfs(curr):
            if curr in hashMap:
                return hashMap[curr]
            
            if curr is None:
                return
            nodeCopy = Node(curr.val)
            hashMap[curr] = nodeCopy
            for neighbor in curr.neighbors:
                nodeCopy.neighbors.append(dfs(neighbor))
            return nodeCopy

        return dfs(node)



