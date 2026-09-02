class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if len(seen) == 0:
            return 0
        ans = 1
        for num in nums:
            # beginning of a sequence
            if (num-1) not in seen:
                sequence = 0
                curr = num
                while curr in seen:
                    sequence += 1
                    curr += 1
                ans = max(sequence, ans)
        return ans