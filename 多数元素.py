# -*- coding: utf-8 -*-
# @Time : 2024/9/22 18:24
# @Author : CSR
# @File : 多数元素.py

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] += 1
            if temp[num] > len(nums) / 2:
                return num