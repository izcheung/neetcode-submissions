from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = Counter(nums)
        sortedAns = sorted(ans.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(sortedAns[i][0])
        return ans
