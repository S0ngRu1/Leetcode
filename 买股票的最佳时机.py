# -*- coding: utf-8 -*-
# @Time : 2024/9/24 19:59
# @Author : CSR
# @File : 买股票的最佳时机.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    prices = [3,2,1]
    print(Solution().maxProfit(prices))