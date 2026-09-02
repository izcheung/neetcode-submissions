"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
         
        def traverse(node):
            if not node:
                return None
           
            if node in seen:
                return seen[node]
        
            root = Node(node.val)
            seen[node] = root
            for neighbor in node.neighbors:
                subsequent = traverse(neighbor)
                root.neighbors.append(subsequent)
            return root
        
     
        return traverse(node)

