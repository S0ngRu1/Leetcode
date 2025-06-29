# -*- coding: utf-8 -*-
# @Time : 2025/6/29 14:10
# @Author : CSR
# @File : pythonday3.py

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 使用pandas读取CSV文件
# 'pd' 是 pandas 的标准别名
df = pd.read_csv('douban_top250_movies.csv')

# --- 检查数据 ---

# 1. 查看前5行数据，对内容有个大致了解
print("数据前5行预览:")
print(df.head())

# 2. 查看数据的基本信息，检查是否有缺失值、数据类型是否正确
print("\n数据基本信息:")
df.info()

# 3. 对 '评分' 列进行描述性统计，看看最大、最小、平均值等
print("\n评分列统计信息:")
print(df['评分'].describe())

df['评分'] = pd.to_numeric(df['评分'])

# 再次检查数据类型，确认转换成功
print("\n清洗后数据基本信息:")
df.info()




# --- 关键步骤：解决Matplotlib中文显示问题 ---
# Matplotlib 默认不支持中文，我们需要指定一个支持中文的字体。
# 'SimHei' 是一个常用的黑体字，请确保你的系统中有此字体，或替换为其他可用中文字体。
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 1. 选取数据：我们只需要前15部电影
top_15 = df.head(15)

# 2. 创建画布和子图，并指定画布大小
# figsize的单位是英寸，(15, 8) 表示一个 15x8 英寸的图
plt.figure(figsize=(15, 8))

# 3. 绘制柱状图
bars = plt.bar(top_15['电影名'], top_15['评分'], color='deepskyblue')

# 4. 添加装饰和细节
plt.title('豆瓣电影Top 15评分', fontsize=20)
plt.xlabel('电影名称', fontsize=14)
plt.ylabel('评分', fontsize=14)
plt.xticks(rotation=45, ha="right") # 让x轴的标签旋转45度，防止重叠
plt.ylim(9.0, 9.8) # 设置Y轴的范围，让微小差异更明显

# 5. 在每个柱子上方显示具体的评分数值
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.01, f'{yval}', ha='center', va='bottom', fontsize=11)

plt.tight_layout() # 自动调整布局，防止标签被截断
plt.show() # 显示图表



# 绘制电影评分分布直方图
plt.figure(figsize=(10, 6))

# bins参数指定将数据划分成多少个区间
plt.hist(df['评分'], bins=25, edgecolor='black', alpha=0.75, color='mediumseagreen')

# 添加一条表示平均分的垂直线
mean_rating = df['评分'].mean()
plt.axvline(mean_rating, color='red', linestyle='dashed', linewidth=2)
# 添加文本来解释这条线
plt.text(mean_rating + 0.01, 30, f'平均分: {mean_rating:.2f}', color='red')

plt.title('豆瓣Top250电影评分分布', fontsize=16)
plt.xlabel('评分区间', fontsize=12)
plt.ylabel('电影数量', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6) # 添加网格线
plt.show()


# 将所有电影标题合并成一个长字符串
text = " ".join(title for title in df['电影名'])

# 创建词云对象，并进行详细配置
# font_path 是必须的，因为它需要中文字体来渲染中文词语
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/SimHei.ttf', # 替换为你系统中可用的中文字体路径
    background_color="white",
    width=800,
    height=600,
    max_words=100,
    contour_width=3,
    contour_color='steelblue'
).generate(text)

# 使用matplotlib来显示生成的词云图
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") # 关闭坐标轴
plt.show()