class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum you can have is len(piles)
        # maximum would be the max pile
        # # of bananas / k
        '''
        [1,4,3,2]
        9

        '''

        l = 1
        r = max(piles)
        ans = float('inf')

        while l <= r:
            mid = (l+r) // 2
            if self.checkK(mid, piles, h):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
            

    def checkK(self, k, piles, h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
            if hours > h:
                return False
        return True
