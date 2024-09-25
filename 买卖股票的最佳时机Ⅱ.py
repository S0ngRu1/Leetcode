# -*- coding: utf-8 -*-
# @Time : 2024/9/25 21:07
# @Author : CSR
# @File : 买卖股票的最佳时机Ⅱ.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1] :
                profit += prices[i] - prices[i - 1]
        return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
