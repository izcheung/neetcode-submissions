from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic stack with sliding window - decreasing order
        q = deque()
        l = 0
        ans = []

        '''
        1,2,1,0,4,2,6
                 l   r
        k=3

        q = [6]

        ans [2, 2, 4, 4, 6]

        '''
        for r in range(len(nums)):
            # generate the monotonic stack
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r >= k - 1):
                maxi = q[0]
                ans.append(nums[maxi])
                l += 1
            
        return ans



