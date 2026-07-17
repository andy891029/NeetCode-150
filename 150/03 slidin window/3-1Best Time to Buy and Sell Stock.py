#prices = [10,1,5,6,7,1]
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        money = 0
        left = 0;right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right 
            else:
                profit = prices[right] - prices[left]
                money = max(money,profit)
            right += 1
        return money
#print(Solution().maxProfit(prices))