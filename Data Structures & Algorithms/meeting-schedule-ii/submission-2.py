"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()

        i = 0
        j = 0

        maxRoom = 0
        count = 0

        while i < len(startTimes) and j < len(endTimes):
            if startTimes[i] < endTimes[j]:
                count += 1
                maxRoom = max(count, maxRoom)
                i += 1
            else:
                count -= 1
                j += 1
        return maxRoom

