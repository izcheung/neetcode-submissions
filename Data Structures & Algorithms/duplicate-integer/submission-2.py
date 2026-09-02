class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set to check for duplicates
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False