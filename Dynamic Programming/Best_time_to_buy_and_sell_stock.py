class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #         Greedy Approach
        #         if len(prices) < 2: return 0

        #         buy = prices[0]
        #         profit = 0

        #         for i in range(1,len(prices)):
        #             if prices[i] - buy > profit:
        #                 profit = prices[i] - buy
        #             if prices[i] < buy:
        #                 buy = prices[i]

        # Dynamic Programming Approach
        if len(prices) < 2: return 0

        profit = [0] * len(prices)
        minimum_price = float('inf')

        for i in range(len(prices)):
            minimum_price = min(minimum_price, prices[i])
            if i == 0: continue
            profit[i] = max(profit[i - 1], prices[i] - minimum_price)
        return profit[-1]
