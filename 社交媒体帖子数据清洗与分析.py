# -*- coding: utf-8 -*-
# @Time : 2025/6/24 21:33
# @Author : CSR
# @File : 社交媒体帖子数据清洗与分析.py


import re
import pandas as pd
from collections import Counter

def clean_text(text):
    text = re.sub("https?\w+",'',text)
    text = re.sub("@\w+",'',text)
    text = re.sub("<\w+>",'',text)
    text = re.sub("[^\w\s]+",'',text)
    text = text.lower()
    return text

def process_data(data_for_process):
    df = pd.DataFrame(data_for_process)
    # 数据清洗
    df['cleaned_text'] = df['text'].apply(clean_text)
    print(df['cleaned_text'])
    # 数据提取
    df['hashtags'] = df['text'].apply(lambda x: re.findall('#(\w+)',x))
    print(df['hashtags'])
    df['word_count'] = df['cleaned_text'].apply(lambda x: len(x.split()))
    print(df['word_count'])
    # 数据分析
    print(df['likes'].nlargest(5,'all'))
    all_hashtags = [tag  for tags in df['hashtags'] for tag in tags]
    all_hashtags_count = Counter(all_hashtags)
    print(all_hashtags_count)
    df.to_csv('text.csv',index=False)


if __name__ == "__main__":
    data = {
        'post_id': [1, 2, 3, 4, 5, 6],
        'user': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'text': [
            'Just finished my #NLP project! So excited! Check it out at https://example.com/project1. What a journey!  #DataScience',
            'Having a great coffee @CafeDelight ☕. The best way to start a day. #MorningVibes',
            'OMG! I can\'t believe I won the lottery! 勞 This is unreal! #Blessed #Lucky',
            'My new blog post on Regular Expressions is live: https://myblog.dev/regex-tutorial. Hope @user456 finds it useful. <br> #Python',
            'What a beautiful sunset...  #Nature #Photography',
            'Feeling a bit under the weather today. 裸 #SickDay. Just want to sleep.'
        ],
        'likes': [152, 88, 1200, 310, 540, 45]
    }
    process_data(data)