# -*- coding: utf-8 -*-
# @Time : 2024/9/21 23:42
# @Author : CSR
# @File : modeltest.py

import unittest

from 删除有序数组中的重复项2 import Solution as RD2


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = RD2()
        nums = [1, 1, 1, 2, 2, 2, 3]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
