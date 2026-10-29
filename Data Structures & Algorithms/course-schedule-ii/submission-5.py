class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        cycle = set()
        completed = set()
        path = []

        def dfs(course):
            if course in cycle:
                return False
        
            if course in completed:
                return True
                
            cycle.add(course)
        
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            completed.add(course)
            path.append(course)

            return True
            
        for course in preMap:
            if not dfs(course):
                return []
        return path
