class Solution:
    def jump(self, nums: List[int]) -> int:

   
        queue = deque([0])
        seen = set()
        num_jumps = 0
        while queue:
            for i in range(len(queue)):
                index = queue.popleft()
                if index == len(nums)-1:
                    return num_jumps
                for j in range(index+1, index + nums[index] + 1):
                    if j not in seen:
                        queue.append(j)
                    seen.add(j)
            num_jumps += 1

