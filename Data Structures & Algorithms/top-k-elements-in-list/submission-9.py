class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        # will have the counts
        # convert the dict to a sorted tuple list (by the first index - freq)
        tuple_list = sorted(list(counter.items()), key=lambda item:item[1])
        k_values = tuple_list[len(tuple_list)-k:]
        return [value[0] for value in k_values]

