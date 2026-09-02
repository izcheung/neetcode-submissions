class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed <= maxSpeed:
            mid = (minSpeed + maxSpeed) //2
            hours = 0
            for pile in piles:
                hours += -(-pile//mid)
            if hours > h:
                minSpeed = mid + 1
            else:
                maxSpeed = mid - 1
        return minSpeed

