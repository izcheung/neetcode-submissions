class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        '''
        [30,38,30,36,35,40,28]
                   r
        stack = [(1,38), (2,30), ]
        ans = [1,0,1,0,0,0,0]

        '''

        for r in range(len(temperatures)):
            while stack and temperatures[r] > stack[-1][1]:
                stackIndx, temp = stack.pop()
                difference = r - stackIndx
                ans[stackIndx] = difference
            stack.append((r, temperatures[r]))
        return ans

