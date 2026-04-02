class Solution(object):
  def maxProfit(self, prices):
    minPrice = prices[0]
    best_profit = 0

    for price in prices:
      if minPrice > price:
        minPrice = price

      if (price > minPrice) and (best_profit < (price - minPrice)):
        best_profit = (price - minPrice)
    
    return best_profit