# -*- coding: utf-8 -*-
# @Time : 2024/9/18 21:51
# @Author : CSR
# @File : 移除元素.py

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # temp = []
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         temp.append(nums[i])
        # print(f'{len(temp)}, nums = {temp}')
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        print(nums)
        return len(nums)
if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums,val))