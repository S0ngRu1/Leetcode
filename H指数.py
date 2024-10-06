# -*- coding: utf-8 -*-
# @Time : 2024/10/6 17:04
# @Author : CSR
# @File : H指数.py

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i

        return 0