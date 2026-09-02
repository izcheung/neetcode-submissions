class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sorted in ascending order
        # I need to compare the end interval for each array to figure out where to put the newInterval
        # compare the start of the newInterval with the end - I want it to insert into an array that 

        # if greater than both start and end
        res = []
        for i in range(len(intervals)):
            newStart = newInterval[0]
            newEnd = newInterval[1]
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            # append the new interval (because its completely less than current interval)
            if newEnd < currStart:
                res.append(newInterval)
                return res + intervals[i:]
            
            # append the current interval (because its completely less than new interval)

            elif newStart > currEnd:
                res.append(intervals[i])

            else:
                newInterval = [min(newStart,currStart), max(newEnd, currEnd)]
        res.append(newInterval)
        return res
            
