class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []
        newStart, newEnd = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]

            if newStart > end:
                ans.append([start, end])
            
            elif newEnd < start:
                ans.append([newStart, newEnd])
                return ans + intervals[i:]

            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        ans.append([newStart,newEnd])
        return ans

