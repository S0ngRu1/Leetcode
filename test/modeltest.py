# -*- coding: utf-8 -*-
# @Time : 2024/9/21 23:42
# @Author : CSR
# @File : modeltest.py

import unittest

from 删除有序数组中的重复项2 import Solution as RD2
from 多数元素 import Solution as ME
from 跳跃游戏2 import  Solution as JP


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

if __name__ == '__main__':
    unittest.main()
