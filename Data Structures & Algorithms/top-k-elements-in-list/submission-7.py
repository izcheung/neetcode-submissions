
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = (len(nums)+ 1) * [None]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, freq in count.items():
            if bucket_sort[freq] is None:
                bucket_sort[freq] = []
            bucket_sort[freq].append(key)
    
        pointer = len(bucket_sort)-1
        ans = []
        while k > 0:
            if bucket_sort[pointer] is not None:
                while len(bucket_sort[pointer]) > 0 and k > 0:
                    ans.append(bucket_sort[pointer].pop())
                    k -= 1
            pointer -= 1
        return ans





