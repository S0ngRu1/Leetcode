# -*- coding: utf-8 -*-
# @Time : 2025/6/27 23:33
# @Author : CSR
# @File : pythonday2.py
import random
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time


def parse_html(html):
    """使用BeautifulSoup解析HTML，提取电影数据"""
    soup = BeautifulSoup(html, 'html.parser')

    # 根据我们之前的分析，找到所有包含电影信息的div
    movie_items = soup.find_all('div', class_='item')
    movies_data = []
    for item in movie_items:
        # .find() 用于在当前标签下查找第一个匹配的子标签
        # .get_text() 用于获取标签内的文本内容
        rank = item.find('em').get_text()
        title = item.find('span', class_='title').get_text()
        rating = item.find('span', class_='rating_num').get_text()
        # 引语可能不存在，需要做个判断
        quote_tag  = item.find('p', class_='quote')
        quote = quote_tag.get_text().strip() if quote_tag else "无"

        movie = {
            '排名': rank,
            '电影名': title,
            '评分': rating,
            '引语': quote
        }
        movies_data.append(movie)

    return movies_data

def fetch_page(url):
    """发送GET请求，获取页面HTML内容"""
    # 伪装成浏览器，添加User-Agent头，否则可能被网站拒绝
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        # 确保请求成功
        if response.status_code == 200:
            return response.text
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"请求异常: {e}")
        return None


def save_to_csv(data, filename='douban_movies.csv'):
    """将数据写入CSV文件"""
    # 'w' 是写入模式, newline='' 防止出现空行, encoding='utf-8-sig' 确保中文在Excel中正常显示
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        # 定义表头
        fieldnames = ['排名', '电影名', '评分', '引语']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # 写入表头
        writer.writeheader()
        # 写入数据行
        writer.writerows(data)
    print(f"数据成功保存到 {filename}")

def save_to_csv_by_pandas(data, filename='douban_movies.csv'):
    """使用pandas将数据写入CSV文件"""
    # DataFrame是pandas处理表格数据的核心数据结构
    df = pd.DataFrame(data)
    # 将DataFrame写入CSV文件
    # to_csv参数说明:
    # - filename: 输出文件名
    # - index=False: 不写入行索引(不保存0,1,2...这样的行号)
    # - encoding: 文件编码(如果需要Excel兼容中文可改为'utf-8-sig')
    df.to_csv(filename,index=False, encoding='utf-8')


def main():
    """主执行函数"""
    all_movies = []
    # Top250共有10页，start参数从0到225，每次增加25
    for i in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={i}&filter='
        print(f"正在抓取页面: {url}")

        html = fetch_page(url)
        if html:
            movies_on_page = parse_html(html)
            all_movies.extend(movies_on_page)
            # 友好爬虫：每抓取一个页面，随机暂停1-3秒，避免给服务器造成太大压力
            sleep_time = random.randint(1, 3)
            print(f"暂停 {sleep_time:.2f} 秒...")
            time.sleep(sleep_time)

    save_to_csv(all_movies, 'douban_top250_movies.csv')



if __name__ == '__main__':
    main()