class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a min heap - keeps the smallest value at the top of the tree where it can be popped
        # [1,2,1,3,3,3], k = 2
        #.       ^
        # heap = [2, 3
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [(value, key) for key, value in count.items()]

        heap = []
        for number in freq:
            heapq.heappush(heap, number)
            if len(heap) > k:
                heapq.heappop(heap)

        return [ pair[1] for pair in heap]
