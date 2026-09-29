import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap, you want to keep the heap at size k
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]