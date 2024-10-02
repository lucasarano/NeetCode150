class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            profit = max(profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
                print("set i to" + str(j))
            j+= 1
        return profit
