class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # keep track of lowest price so far
        max_profit = 0             # result

        for price in prices:
            min_price = min(min_price, price)           # update min price
            max_profit = max(max_profit, price - min_price)  # profit if sold today

        return max_profit