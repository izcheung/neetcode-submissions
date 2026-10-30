class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i : i[0])

        ans = 0

        prevEndInterval = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEndInterval:
                ans += 1
                prevEndInterval = min(prevEndInterval, end)
            else:
                prevEndInterval = end
        return ans
            