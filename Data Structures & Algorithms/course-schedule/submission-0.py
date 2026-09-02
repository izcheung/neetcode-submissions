class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build an adjacency list dictionary from prerequisites - 
        # build a graph with the relationships (directed)
        
        def hasCycle(graph, node, visiting, visited) -> bool: #true if has cycle
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)
            
            for neighbour in graph[node]:
                if hasCycle(graph, neighbour, visiting, visited):
                    return True
            
            visiting.remove(node)

            visited.add(node)

            return False



        def buildGraph(prereqs, numCourses):
            graph = {}
            for i in range(numCourses):
                graph[i] = []
            
            # {0: [1], 1:[2]}
            for prereq in prereqs: #[0,1]
                a, b = prereq # b->a
                graph[a].append(b)
            return graph

        
        graph = buildGraph(prerequisites, numCourses)
        # iterate through all the nodes in the graph and try to see if there is a cycle
        for node in graph:
            if hasCycle(graph, node, set(), set()):
                return False
        return True





