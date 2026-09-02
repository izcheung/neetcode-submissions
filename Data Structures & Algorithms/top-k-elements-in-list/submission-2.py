from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count it with hashmap
        # Use max heap

        # 1. Count with hashmap
        # 2. save into a list as a (count, number) tuple
        # 3. Pop k times

# nums = [1,2,2,3,3,3], k = 2
        counter = Counter(nums) #{1: 1, 2: 2, 3: 3}

        counterArray = []
        for key, value in counter.items():
            counterArray.append((value, key))
        counterArray.sort() #[(1,1), (2,2), (3,3)]

        ans = []
        for i in range(k):
            counter, key = counterArray.pop()
            ans.append(key)
        return ans




    

        
