class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # fully explore one island - return boolean if its new - in the outer function return true

        def buildGraph():
            graph = {}
            for i in range(n):
                graph[i] = []
            for edge in edges:
                a,b = edge
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph = buildGraph()
        visited = set()

        def explore(graph, node, visited):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in graph[node]:
                explore(graph, neighbour, visited)
            return True

        count = 0
        for node in graph:
            if explore(graph, node, visited):
                count += 1
        return count


            
