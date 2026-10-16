class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # backtracking path

        # First build a adj list
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        path = []
        visiting = set()
        cycle = set()

        def dfs(course):
    
            if course in cycle:
                return False
            if course in visiting:
                return True
                
            cycle.add(course)
        
            for each in preMap[course]:
                if not dfs(each):
                    return False
            
            cycle.remove(course)

            visiting.add(course)
            path.append(course)

            return True
            
            
        for course in preMap:
            if not dfs(course):
                return []
        return path
