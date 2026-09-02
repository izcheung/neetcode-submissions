class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # ensure that the largest small is less than smallest in large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            # pop from small and add to large
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

        
        # len should be at most 1 different
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
        
        