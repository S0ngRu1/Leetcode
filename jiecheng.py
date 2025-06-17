# -*- coding: utf-8 -*-
# @Time : 2025/6/17 21:12
# @Author : CSR
# @File : jiecheng.py

def jiecheng1(n :int ):
    if n == 0:
        return 1
    else:
        return n * jiecheng1(n-1)

def jiecheng2(n :int ):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res


if __name__ == '__main__':
    print(jiecheng1(5))