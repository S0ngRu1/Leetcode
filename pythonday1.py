# -*- coding: utf-8 -*-
# @Time : 2025/6/26 20:48
# @Author : CSR
# @File : pythonday1.py
# import re
# import sys
#
# def read_file(file_path):
#     """读取文件内容并返回文本字符串"""
#     try:
#         # 'with' 语句能确保文件在操作完成后被正确关闭，即使发生错误。
#         # 'r' 表示读取模式, 'utf-8' 是推荐的文本编码。
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"错误: 文件 '{file_path}' 未找到。")
#         # 退出程序，状态码 1 表示有错误发生。
#         sys.exit(1)
#
#
# def count_words(text):
#     """统计文本中每个单词的频率"""
#     # 1. 全部转为小写
#     text = text.lower()
#
#     # 2. 使用正则表达式替换所有非字母数字的字符为空格
#     # [^a-z0-9\s] 匹配任何不是小写字母、数字或空白字符的字符
#     text = re.sub(r'[^a-z0-9\s]', ' ', text)
#
#     # 3. 按空白字符分割成单词列表
#     words = text.split()
#
#     # 4. 统计词频
#     word_counts = {}
#     for word in words:
#         # dict.get(key, default) 是一个安全获取值的方法
#         # 如果 word 已在字典中，返回其值并+1；否则返回默认值0，再+1。
#         word_counts[word] = word_counts.get(word, 0) + 1
#
#     return word_counts
#
# # --- 主程序入口 ---
# if __name__ == '__main__':
#     file_path = 'article.txt'
#     top_n = 5  # 前 5 个 词频最高的词
#
#     text_content = read_file(file_path)
#     word_freq = count_words(text_content)
#
#     # 对字典按值进行排序
#     # word_freq.items() 将字典转为 (key, value) 元组的列表
#     # sorted() 函数进行排序
#     # key=lambda item: item[1] 指定按每个元组的第二个元素（也就是词频）排序
#     # reverse=True 表示降序
#     sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
#
#     # 输出前 N 个结果
#     print(f"文件 '{file_path}' 中词频最高的 {top_n} 个单词是:")
#     for word, count in sorted_words[:top_n]:
#         print(f"- {word}: {count}")


import sys
import re
from collections import Counter


def main():
    # 1. 解析命令行参数
    if len(sys.argv) != 3:
        print("使用方法: python word_counter.py <文件路径> <数量N>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        top_n = int(sys.argv[2])
    except ValueError:
        print("错误: 数量N必须是一个整数。")
        sys.exit(1)

    # 2. 读取文件
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
        sys.exit(1)

    # 3. 文本清洗和分割
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    words = text.split()

    # 4. 使用 Counter 进行词频统计
    word_counts = Counter(words)

    # 5. 获取最常见的 N 个单词
    # Counter.most_common(n) 是一个非常方便的方法
    top_words = word_counts.most_common(top_n)

    # 6. 打印结果
    print(f"文件 '{file_path}' 中词频最高的 {top_n} 个单词是:")
    for word, count in top_words:
        print(f"- {word}: {count}")


if __name__ == '__main__':
    main()