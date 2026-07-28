class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                # Update lowest buying price seen so far
                min_price = price
            elif price - min_price > max_profit:
                # Update maximum profit if selling today gives a higher return
                max_profit = price - min_price
                
        return max_profit