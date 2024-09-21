# -*- coding: utf-8 -*-
# @Time : 2024/9/21 22:27
# @Author : CSR
# @File : 删除有序数组中的重复项2.py

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                temp += 1
            else:
                temp = 1
            if temp > 2:
                del nums[i]
                temp -= 1
        return len(nums)
