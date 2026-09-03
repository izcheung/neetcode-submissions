class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 indexed
        # hashmap - but cannot use because we must use O(1) space
        '''
        so just basically using variables
        special note - the array is in non decreasing order
        so just use two pointer - i and j (start on either ends)
        fulfills the just using variables

        target = 5
        [1,1,2,3,6]

        also note it is 1 index so when returning the ans account for that
        '''
        i = 0
        j = len(numbers)-1
        while i < j:
            total = numbers[i] + numbers[j]
            if total > target:
                j -= 1
            elif total == target:
                return [i+1, j+1]
            else:
                # less than
                i += 1


