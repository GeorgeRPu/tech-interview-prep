r"""
>>> from best_time_to_buy_and_sell_stock__one_pass import maxProfit
>>> maxProfit([7, 1, 5, 3, 6, 4])
5
>>> maxProfit([7, 6, 4, 3, 1])
0
"""


def maxProfit(prices: list[int]) -> int:
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
