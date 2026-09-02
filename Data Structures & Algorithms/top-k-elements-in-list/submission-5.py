
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap, sort by their value and return their key, sort based
        freq = {} 
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        sortedData = sorted(freq.items(), key=lambda item:item[1])
        ans = []
        while k > 0:
            key, freq = sortedData.pop()
            ans.append(key)
            k -= 1
        return ans

