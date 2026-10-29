class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
   
        graph = {i:[] for i in range(n)}
        seen = set()

        for edge in edges:
            a,b = edge
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            if node in seen:
                return False

            seen.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
            
        if not dfs(0, None):
            return False
            
        if len(seen) != len(graph):
            return False
        return True