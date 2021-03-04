class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_array = [0]*(amount+1)

        for i in range(1,amount+1):
            minimum = float('inf')
            for j in range(len(coins)):
                if i >= coins[j]:
                    minimum = min(minimum, 1+dp_array[i-coins[j]])
            dp_array[i] = minimum
        if dp_array[amount] == float('inf'):return -1
        return dp_array[amount]
