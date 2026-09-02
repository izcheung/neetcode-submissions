class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count up all the frequencies using a hashmap
        # Put the numbers into its respective bucket
        # bucket sort, the index of the array corresponds to the freq
        # iterate through the freq array backwards to get k elements
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)


        
        # The highest freq it can be is the len of nums
        bucket = [[] for i in range(len(nums) + 1)]


        # {1: 3, 2: 2, 3: 1}
        #  ^

        for key, value in counter.items():
            bucket[value].append(key)
        
        # bucket = [[],[3],[2],[]]
        # 3, 2, 1, 0
        # k = 1
        # result, 1,2

        result = []
        
        for i in range(len(bucket)-1, -1, -1):
            while len(bucket[i]) > 0 and k > 0:
                result.append(bucket[i].pop())
                k -= 1
        return result



