# -*- coding: utf-8 -*-
# @Time : 2025/6/29 21:23
# @Author : CSR
# @File : app.py.py

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    """这个函数被称为“视图函数”(view function)"""
    return '<h1>Hello, Web World!</h1>'

@app.route('/index/')
def index():
    # 1. 使用pandas读取我们的电影数据
    df = pd.read_csv('douban_top250_movies.csv')

    # 2. 将整个DataFrame转换为HTML表格字符串
    #    - classes: 为表格添加CSS类，方便后续美化（我们后面会用Bootstrap）
    #    - index=False: 不显示DataFrame的索引列
    movie_table = df.to_html(classes='table table-striped table-hover', index=False)

    # 3. 渲染模板，并传递数据
    #    - 'index.html': 我们要渲染的HTML文件名
    #    - movie_table=movie_table: 将Python中的变量movie_table传递给HTML，
    #      在HTML中它也叫'movie_table'
    return render_template('index.html', movie_table=movie_table)


if __name__ == '__main__':
    app.run(debug=True)