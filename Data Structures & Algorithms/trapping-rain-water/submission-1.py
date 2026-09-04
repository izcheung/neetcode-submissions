class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
  
        '''
        [0,2,0,3,1,0,1,3,2,1]

        leftMax = [0,2,0,0,0,0,0,0,0,0]
        rightMax = [0,0,0,0,0,0,0,0,0,0]
        '''
        
        maxCurrLeft = height[0]
        maxCurrRight = height[-1]

        lenArr = len(height)

        for i in range(0, len(height)):
            maxCurrLeft = max(maxCurrLeft, height[i])
            leftMax[i] = maxCurrLeft

        for i in range(len(height)-1, -1,-1):
            maxCurrRight = max(maxCurrRight, height[i])
            rightMax[i] = maxCurrRight

        ans = 0
        for i in range(len(leftMax)):
            ans += min(leftMax[i], rightMax[i]) - height[i]
        return ans
