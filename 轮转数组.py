# -*- coding: utf-8 -*-
# @Time : 2024/9/23 21:11
# @Author : CSR
# @File : 轮转数组.py

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(Solution().rotate(nums,k))
