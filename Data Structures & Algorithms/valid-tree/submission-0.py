class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree cannot have loops
        # Tree must be all connected

        # start from any point
        
        if len(edges) > (n-1):
            return False

        def buildGraph(edges, n):
            graph = {}
            for i in range(n):
                graph[i] = []
            for edge in edges:
                a,b = edge
                graph[a].append(b)
                graph[b].append(a)

            return graph


        def hasCycle(graph, node, parent, visited):

            if node in visited:
                return False

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                if hasCycle(graph, neighbour, node, visited):
                    return True

            return False


        graph = buildGraph(edges, n)

        visited = set()

        if hasCycle(graph, 0, -1, visited):
            return False
        return n == len(visited)




