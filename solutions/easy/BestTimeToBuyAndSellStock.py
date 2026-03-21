r"""
Problem
-------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array ``prices`` where ``prices[i]`` is the price of a
given stock on the ``i``\ :sup:```th``` day.

You want to maximize your profit by choosing a **single day** to buy one
stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If
you cannot achieve any profit, return ``0``.

 

**Example 1:**

::


   Input: prices = [7,1,5,3,6,4]
   Output: 5
   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

::


   Input: prices = [7,6,4,3,1]
   Output: 0
   Explanation: In this case, no transactions are done and the max profit = 0.

 

**Constraints:**

- ``1 <= prices.length <= 10``\ :sup:```5```
- ``0 <= prices[i] <= 10``\ :sup:```4```

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

Pattern
-------
Array, Dynamic Programming

Code
----

.. literalinclude:: ../solutions/easy/BestTimeToBuyAndSellStock.py
    :language: python
    :lines: 80-

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
