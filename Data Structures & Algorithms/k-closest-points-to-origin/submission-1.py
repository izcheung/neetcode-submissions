class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Loop through the array, calculate the distance using the equation, add it to a heap (min heap)
        # At the end, pop k values 
        # In the heap maybe i can have a tuple with the (distance, [,]) sort by distance
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(heap, (distance, point))
        ans = []
        for i in range(k):
            val, point = heapq.heappop(heap)
            ans.append(point)
        return ans
