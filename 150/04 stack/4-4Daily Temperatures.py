#temperatures = [30,38,30,36,35,40,28]
'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        for day in range(len(temperatures)):
            for future in range(day+1,len(temperatures)):
                if temperatures[day] < temperatures[future]:
                    ans[day] += (future - day) 
                    break
        return ans
'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        not_find = []
        for day in range(len(temperatures)):
            while not_find and temperatures[day] > temperatures[not_find[-1]]:
                ans[not_find[-1]] = (day - not_find[-1])
                not_find.pop()
            not_find.append(day)
        return ans
#print(Solution().dailyTemperatures(temperatures)) 