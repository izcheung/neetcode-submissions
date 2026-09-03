class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start with max width -> l and r pointer
        # move the pointer with the lower value -> to maximize the value
        # two pointer
        # keep track of the max value
        l = 0
        r = len(heights)-1
        max_height = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_height = max(area, max_height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_height
