# -*- coding: utf-8 -*-
# @Time : 2024/9/27 22:21
# @Author : CSR
# @File : 跳跃游戏2.py
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = len(nums) - 1
        step = 0
        while position > 0:
            for i in range(position):
                if nums[i] + i >= position:
                    position = i
                    step += 1
                    break

        return step

if __name__ == '__main__':
    nums = [1,2,1,1,1]
    print(Solution().jump(nums))
