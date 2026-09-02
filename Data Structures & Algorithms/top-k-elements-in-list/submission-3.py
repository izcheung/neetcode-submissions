class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap
        # remember to multiply by -1


 

        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        minHeap = []

        for key, value in counter.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        ans = []
        for i in range(len(minHeap)):
            ans.append(minHeap[i][1])
        return ans