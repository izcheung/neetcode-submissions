class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [2,3,4]
             lr
         l = 0
         r = 2
         mid = (1)

        '''
        for i, num in enumerate(numbers):
            need = target - num
            l = i + 1
            r = len(numbers)-1
            while l <= r:
                mid = (l + r) // 2
                mid_num = numbers[mid]
                if mid_num > need:
                    r = mid - 1
                elif mid_num < need:
                    l = mid + 1
                else:
                    return [i+1, mid+1]

        