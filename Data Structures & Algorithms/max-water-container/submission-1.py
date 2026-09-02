# similar approach to three sum
# nevermind, I cannot because the array is not sorted, so i dont whether to move the j or k pointer
# Also, i just need two pointers
# Let's try brute force first
'''
    Use a for loop on the outer loop
    Use while loop on the inner loop
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        maxArea = 0
        j = len(heights)-1
        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            maxArea = max(area, maxArea)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea





        # # cannot scramble the array (no sorting allowed)
        # maxWater = 0
        # # find the length using the index (r index - l index)
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j-i)
        #         maxWater = max(area, maxWater)
        # return maxWater

