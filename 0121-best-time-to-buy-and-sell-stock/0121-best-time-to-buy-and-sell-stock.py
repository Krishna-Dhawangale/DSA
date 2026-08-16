class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        bestbuy = prices[0]

        for i in range(len(prices)):
            if prices[i] > bestbuy:
                max_profit = max(max_profit, prices[i] - bestbuy)
            bestbuy = min(bestbuy, prices[i])

        return max_profit