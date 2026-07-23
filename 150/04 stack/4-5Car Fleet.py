target = 10; position = [4,1,0,7]; speed = [2,2,1,1]
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        distance = [0]*len(position)
        time = [0]*len(position)
        stack = []
        ans = len(position)
        cars = []
        for i in range (len(position)):
            distance[i] = target - position[i]
            time[i] = distance[i]/speed[i]
            cars.append((position[i],time[i]))
        cars.sort()
        for i in range (len(cars)-1,-1,-1):
            if not stack:
                stack.append(cars[i][1])
                continue
            if cars[i][1] <= stack[-1]:
                ans -= 1
            else:
                stack.append(cars[i][1])
            
        return ans

print(Solution().carFleet(target,position,speed))