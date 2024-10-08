# -*- coding: utf-8 -*-
# @Time : 2024/10/8 20:45
# @Author : CSR
# @File : 除自身以外数组的乘积.py
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
#         L和R分别表示左右两侧的乘积列表
        L, R, answer = [0] * n, [0] * n, [0] * n
        # L[i]表示nums[0:i]的乘积
        L[0] = 1
        for i in range(1, n):
            print(i)
            L[i] = nums[i - 1] * L[i - 1]
        # R[i]表示nums[i:n]的乘积
        R[n - 1] = 1
        print('--------------------------------------')
        for i in reversed(range(n - 1)):
            print(i)
            R[i] = nums[i + 1] * R[i + 1]
        # answer[i] = L[i] * R[i]
        # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        for i in range(n):
            answer[i] = L[i] * R[i]

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))
