class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if preMap[course] == []:
                return True

            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            preMap[course] = []
            visiting.remove(course)
            return True

        for c in preMap.keys():
            if not dfs(c):
                return False
        return True
