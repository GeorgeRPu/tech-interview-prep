"""
Problem
-------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Solution
--------
Note that we only need to find the maximum possible profit, not the buy and
sell days which simplifies the problem. We make money by buying low and
selling high. Suppose we buy at price :math:`a`. Then we should sell at the
highest price before it drops below :math:`a`. If ``prices = [1, 3, 2, 4]``,
then we should ignore the temporary drop from 3 to 2 and hold until 4.

Store the price we paid for the stock as ``buy_price`` and the maximum profit
so far as ``max_profit``. We initialize ``max_profit = 0`` and can update each
day. ::

    max_profit = max(price - buy_price, max_profit)

We update ``buy_price`` only when we find a lower price.

Test
----
>>> from BestTimeToBuyAndSellStock import maxProfit
>>> maxProfit([7, 1, 5, 3, 6, 4])
5
>>> maxProfit([7, 6, 4, 3, 1])
0
"""


from typing import List


def maxProfit(prices: List[int]) -> int:
    """Find the maximum profit that can be made by buying and selling a stock
    once on different days.
    """
    max_profit = 0
    buy_price = float('inf')
    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            max_profit = max(price - buy_price, max_profit)
    return max_profit
