# -*- coding: utf-8 -*-
# @Time : 2024/9/20 22:46
# @Author : CSR
# @File : 删除有序数组中的重复项.py


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        print(nums)
        return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))