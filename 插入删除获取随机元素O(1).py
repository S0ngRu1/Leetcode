# -*- coding: utf-8 -*-
# @Time : 2024/10/7 10:25
# @Author : CSR
# @File : 插入删除获取随机元素O(1).py
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_1, param_2, param_3)
# param_1 = obj.insert(2)
# param_2 = obj.remove(3)

# param_2 = obj.remove(2)
# param_3 = obj.getRandom()