class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        newArr = []
        for i, num in enumerate(nums):
            newArr.append((num, i))
        newArr.sort()
        l = 0
        r = len(newArr)-1
        while l < r:
            total = newArr[l][0] + newArr[r][0]
            if total == target:
                return [min(newArr[l][1], newArr[r][1]), max(newArr[l][1], newArr[r][1])]
            elif total > target:
                r -= 1
            else:
                l += 1
        return []
    
