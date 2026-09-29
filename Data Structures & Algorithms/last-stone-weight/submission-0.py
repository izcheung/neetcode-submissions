import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap, (first two)
        # push back the difference into the heap
        # order doesn't matter
        heap = []
        heapq.heapify(heap)
        for num in stones:
            heapq.heappush(heap, -num)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            newDifference = abs(first - second)
            heapq.heappush(heap, -newDifference)
        return -heap[0] if len(heap) == 1 else 0


