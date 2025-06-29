# -*- coding: utf-8 -*-
# @Time : 2025/6/29 21:23
# @Author : CSR
# @File : app.py.py

from flask import Flask

# 创建一个Flask应用实例
app = Flask(__name__)

# 定义一个“路由”（route），告诉Flask哪个URL应该触发哪个函数
# '/' 表示网站的根目录（例如 http://127.0.0.1:5000/）
# IP 地址：127.0.0.1（即本机）
# 5000 是 Flask 默认使用的端口号。
@app.route('/')
def hello_world():
    """这个函数被称为“视图函数”(view function)"""
    return '<h1>Hello, Web World!</h1>'

# 确保当脚本被直接执行时，才运行Web服务器
if __name__ == '__main__':
    # app.run() 启动服务器
    # debug=True 表示开启“调试模式”，当代码有改动时服务器会自动重启，并提供详细的错误信息
    app.run(debug=True)