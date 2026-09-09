class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        sortedCars = sorted(cars)

        stack = []
        for i in range(len(sortedCars)-1,-1,-1):
            
            position = sortedCars[i][0]
            speed = sortedCars[i][1]

            targetTime = (target - position) / speed
            stack.append(targetTime)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
          
        return len(stack)