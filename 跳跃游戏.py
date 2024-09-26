# -*- coding: utf-8 -*-
# @Time : 2024/9/26 20:50
# @Author : CSR
# @File : 跳跃游戏.py
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))



