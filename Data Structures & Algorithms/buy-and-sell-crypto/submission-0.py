class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        netprofit = 0
        i = 0
        j = i + 1
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                netprofit = max(profit, netprofit)
            else:
                i = j
            j +=1
        return netprofit
        
        