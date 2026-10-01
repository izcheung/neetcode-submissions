class MedianFinder:
    # Brute force solution - use an array, append the new number, sort it, find if it is odd or even. if odd then find the median using len(array) -> 3//2, if even then (4//2) and index -1 take the average then find the index of the middle number

    # nlogn
    # logn using a heap for keeping things sorted, but then how do you find the median?

# left heap (max heap)
# right heap (min heap)
    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:

        '''
        [-5,-3], 
        '''
        if len(self.leftHeap) > 0 and num > -self.leftHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -num)
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            maxi = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, -maxi)
        elif len(self.rightHeap) - len(self.leftHeap) > 1:
            mini = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -mini)


        
    def findMedian(self) -> float:
        # even number
        if len(self.leftHeap) == len(self.rightHeap):
            first = -self.leftHeap[0]
            second = self.rightHeap[0]
            median = (first + second)/2
            return median
        else:
            if len(self.leftHeap) > len(self.rightHeap):
                return -self.leftHeap[0]
            else:
                return self.rightHeap[0]
        
        