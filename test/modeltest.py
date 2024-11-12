# -*- coding: utf-8 -*-
# @Time : 2024/9/21 23:42
# @Author : CSR
# @File : modeltest.py

import unittest

from 删除有序数组中的重复项2 import Solution as RD2
from 多数元素 import Solution as ME
from 跳跃游戏2 import  Solution as JP
from H指数 import Solution as H
from 分糖果 import Solution as CA

class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = RD2()
        nums = [1, 1, 1, 2, 2, 2, 3]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 5)

    def test_majorityElement(self):
        solution = ME()
        nums = [1, 2, 2, 2, 3]
        result = solution.majorityElement(nums)
        self.assertEqual(result, 2)

    def test_jump(self):
        solution = JP()
        nums = [2, 3, 1, 1, 4]
        result = solution.jump(nums)
        self.assertEqual(result, 2)

    def test_jump2(self):
        solution = JP()
        nums = [2, 3, 0, 1, 4]
        result = solution.jump(nums)
        self.assertEqual(result, 2)

    def test_jump3(self):
        solution = JP()
        nums = [1,2,1,1,1]
        result = solution.jump(nums)
        self.assertEqual(result, 3)
    def test_hIndex(self):
        solution = H()
        citations = [3, 0, 6, 1, 5]
        result = solution.hIndex(citations)
        self.assertEqual(result, 3)

    def test_hIndex2(self):
        solution = H()
        citations = [1, 3, 1]
        result = solution.hIndex(citations)
        self.assertEqual(result, 1)

    def test_candy(self):
        solution = CA()
        citations = [1,2,87,87,87,2,1]
        result = solution.candy(citations)
        self.assertEqual(result, 13)

if __name__ == '__main__':
    unittest.main()
