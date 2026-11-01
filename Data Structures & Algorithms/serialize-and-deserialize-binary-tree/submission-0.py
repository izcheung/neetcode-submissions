# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        path = []

        def dfs(root):
            if not root:
                path.append("N")
                return
            path.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        string = ",".join(path)
        return string
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        path = data.split(',')
        self.i = 0

        def dfs():
            if path[self.i] == "N":
                self.i += 1
                return None
            
            newNode = TreeNode(int(path[self.i]))
            self.i += 1 

            newNode.left = dfs()
            newNode.right = dfs()
            return newNode

        return dfs()


