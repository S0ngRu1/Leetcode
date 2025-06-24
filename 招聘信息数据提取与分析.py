# -*- coding: utf-8 -*-
# @Time : 2025/6/24 22:13
# @Author : CSR
# @File : 招聘信息数据提取与分析.py

"""
1. **加载数据**：使用 Pandas 创建一个 DataFrame 来存储原始数据。
2. **信息提取与清洗**：
    - **a. 清洗职位描述**：职位描述 `description` 列中包含大量 HTML 标签 (例如 `<b>`, `<li>`, `<p>`)。请创建一个新列 `cleaned_desc`，内容为移除了所有 HTML 标签后的纯文本。
    - **b. 提取技能**：
        - 给定一个技能关键词列表 `SKILLS_DB`。
        - 创建一个新列 `skills`，从 `cleaned_desc` 中提取出每个职位所要求的所有技能。**注意**：技能匹配应该不区分大小写。如果一个职位描述中没有提到任何列表中的技能，则该列对应的值应为空列表 `[]`。
    - **c. 提取薪资**：职位描述中可能包含薪资信息，格式不一（如 `$150,000`, `¥95k`, `$120k-$150k`）。创建一个新列 `salary_info`，用正则表达式从中提取出薪资范围的字符串。如果未找到，则该列的值应为 `None`。
3. **数据分析**：
    - **a. 最热门技能统计**：统计所有职位中，需求量排名前 5 的技能是什么？
    - **b. 远程工作机会**：统计有多少个职位提到了“远程办公”或“Remote”？
"""


from collections import Counter
import pandas as pd
import re

# 预定义的技能数据库
SKILLS_DB = [
    'Python', 'Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'PyTorch',
    'SQL', 'NoSQL', 'Spark', 'Hadoop', 'AWS', 'Docker', 'Git'
]

def clean_text(text:str)->str:
    return re.sub(r'<[\w/]+>', '', text)

def process_data(df_for_process:pd.DataFrame):
    # 数据清洗
    df_for_process['cleaned_desc'] = df_for_process['description'].apply(clean_text)
    # 提取技能
    df_for_process['skills'] = df_for_process['cleaned_desc'].apply(lambda x: [skill for skill in SKILLS_DB if skill.lower() in x.lower() ])
    # 薪资信息
    pattern = r'([\$¥]\s*\d[\d,]*k?(?:\s*-\s*[\$¥]?\s*\d[\d,]*k?)?)'
    df_for_process['salary_info'] = df_for_process['cleaned_desc'].str.extract(pattern, expand=False)

    # 数据分析
    all_skills = df.explode('skills')['skills'].dropna()
    top_5_skills = all_skills.value_counts().nlargest(5)
    print(top_5_skills)
    remote_pattern = r'remote|远程办公'
    remote_jobs_count = df['description'].str.contains(remote_pattern, case=False, na=False).sum()
    print(f"总共发现 {remote_jobs_count} 个职位提及远程办公。")
    df.to_csv('test.csv', index=False)
    


if __name__ == '__main__':


    # 模拟的招聘数据
    data = {
        'job_id': [101, 102, 103, 104, 105, 106],
        'title': [
            'Data Scientist', 'Machine Learning Engineer', 'Data Analyst',
            'Senior Python Developer', 'DevOps Engineer', 'Big Data Engineer'
        ],
        'description': [
            '<b>Job Responsibilities:</b><p>We are looking for a data scientist proficient in <ul><li>Python</li><li>Scikit-learn</li><li>SQL</li></ul>. Experience with AWS is a plus. Salary range is $120,000 - $150,000 per year.</p>',
            '<li>Requirements: Strong experience in <b>pytorch</b> or <b>tensorflow</b>. Must know advanced python.</li><p>This is a fully <b>Remote</b> position.</p>',
            'We need a data analyst with excellent SQL and Pandas skills. <p>Salary: ¥30k-40k per month.</p>',
            'Senior developer needed. <b>Must have:</b> 5+ years of python, git. Salary is around $160k.',
            'Seeking a DevOps expert with hands-on experience in <b>Docker</b> and <b>AWS</b>. Scripting with python is essential. No salary info provided.',
            '<p>Required skills: Spark, Hadoop, and advanced SQL. This position can be Remote.</p>'
        ]
    }

    df = pd.DataFrame(data)
    process_data(df)
