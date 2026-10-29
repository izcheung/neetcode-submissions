class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i:[] for i in range(n)}
     
        seen = set()

        for edge in edges:
            a,b = edge
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node in seen:
                return False

            seen.add(node)

            for neighbour in graph[node]:
                dfs(neighbour)
                
            return True

        count = 0
        for node in range(n):
            if dfs(node):
                count += 1
        return count

