# -*- coding: utf-8 -*-
# @Time : 2025/7/3 16:28
# @Author : CSR
# @File : api.py
import json

from flask import Flask, Response, jsonify, request
import pandas as pd

app = Flask(__name__)

# 为防止中文乱码，确保JSON响应使用UTF-8编码
app.config['JSON_AS_ASCII'] = False

# 在应用启动时，一次性将数据加载到内存中，避免每次请求都读取文件
try:
    df = pd.read_csv('douban_top250_movies.csv')
    # 确保评分是数字类型，方便后续可能的操作
    df['评分'] = pd.to_numeric(df['评分'])
except FileNotFoundError:
    print("错误：douban_top250_movies.csv 文件未找到。请先运行Day 2/3的脚本生成数据。")
    df = pd.DataFrame()  # 创建一个空的DataFrame以避免启动失败


@app.route('/')
def home():
    return '<h1>欢迎来到我的豆瓣电影API！</h1><p>请尝试访问 /api/v1/movies 查看所有电影数据。</p><p>请尝试访问 /api/v1/movies/n 查看排名第n的电影数据。</p>'

@app.route('/api/v1/movies', methods=['GET'])
def get_all_movies():
    """返回所有电影的列表"""
    # .to_dict('records') 是pandas的另一个神技，
    # 它能将DataFrame直接转换为一个由字典组成的列表，这正是JSON Array的标准格式。
    movies_list = df.to_dict('records')
    return Response(
        json.dumps(movies_list, ensure_ascii=False, indent=2),
        content_type='application/json; charset=utf-8'
    )


@app.route('/api/v1/movies/<int:rank>', methods=['GET'])
def get_movie_by_rank(rank):
    """根据排名返回单部电影的信息"""
    movie = df[df['排名'] == rank]

    if movie.empty:
        # 返回错误信息（包含中文）也用自定义响应构造
        return app.response_class(
            response=json.dumps({'error': f'未找到排名为 {rank} 的电影。'}, ensure_ascii=False, indent=2),
            mimetype='application/json; charset=utf-8'
        ), 404
    else:
        movie_dict = movie.to_dict('records')[0]
        return app.response_class(
            response=json.dumps(movie_dict, ensure_ascii=False, indent=2),
            mimetype='application/json; charset=utf-8'
        )

@app.route('/api/v1/movies/search', methods=['GET'])
def search_movies():
    """根据查询参数'电影名'来搜索电影"""
    query_title = request.args.get('电影名', '')

    if not query_title:
        return app.response_class(
            response=json.dumps({'error': '请提供要搜索的电影标题。'}, ensure_ascii=False),
            mimetype='application/json; charset=utf-8'
        ), 400

    results = df[df['电影名'].str.contains(query_title, case=False)]

    if results.empty:
        return app.response_class(
            response=json.dumps({'message': f'未找到包含“{query_title}”的电影。'}, ensure_ascii=False),
            mimetype='application/json; charset=utf-8'
        ), 404
    else:
        return app.response_class(
            response=json.dumps(results.to_dict('records'), ensure_ascii=False),
            mimetype='application/json; charset=utf-8'
        )

if __name__ == '__main__':
    app.run(debug=True)