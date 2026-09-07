from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        We use a deque to keep track of the incoming maximums
        whenever there is a new maximum, pop everything before that is less
        to pop from the deque, check if the left pointer is greater than the q[0]
        only append to the result once the window is the right size
        '''
        q = deque()
        result = []

        l = 0
        for r in range(len(nums)):
            currVal = nums[r]
            while q and nums[q[-1]] < currVal:
                q.pop()
            q.append(r)
        
            if l > q[0]:
                q.popleft()

            if (r >= k - 1):
                result.append(nums[q[0]])
                l += 1
        return result