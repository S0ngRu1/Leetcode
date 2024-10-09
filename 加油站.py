# -*- coding: utf-8 -*-
# @Time : 2024/10/9 21:01
# @Author : CSR
# @File : 加油站.py

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank, curr_tank, start = 0, 0, 0

        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:

                start = i + 1
                curr_tank = 0

        if total_tank < 0:
            return -1

        return start

if __name__ == '__main__':
    gas = [2,3,4]
    cost = [3,4,3]
    print(Solution().canCompleteCircuit(gas, cost))