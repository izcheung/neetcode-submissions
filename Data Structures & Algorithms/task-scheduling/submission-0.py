class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # can be any order
        # identical must be separated by n cpu cycles
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        interval = 0
        while maxHeap or q:
            interval += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                if 1 + count < 0:
                    q.append([1+count, interval+n])

            if q and q[0][1] == interval:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return interval
