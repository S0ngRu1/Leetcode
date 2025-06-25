# -*- coding: utf-8 -*-
# @Time : 2025/6/25 21:38
# @Author : CSR
# @File : 解析菜谱配料.py

"""


**任务要求**：

1. **数据加载**：使用下方提供的代码创建初始 DataFrame。
2. **核心解析函数**：
    - 创建一个名为 `parse_ingredients` 的函数，它接收一个配料长字符串（如 `'2 1/2 cups flour; 1 teaspoon salt; ...'`）作为输入。
    - 在函数内部，你需要：
        - **a. 分割**：将长字符串按分号 `;` 分割成单个的配料字符串列表。
        - **b. 提取**：对每一个独立的配料字符串（如 `'2 1/2 cups flour'`），使用正则表达式提取出三个部分：
            - **数量 (quantity)**：如 `2 1/2`, `1`, `0.5`
            - **单位 (unit)**：如 `cups`, `teaspoon`, `g`
            - **名称 (name)**：如 `flour`, `salt`
        - **c. 格式化返回**：函数最终应返回一个**列表**，其中每个元素都是一个包含以上三个信息的**字典**。例如： `[{'quantity': '2 1/2', 'unit': 'cups', 'name': 'flour'}, {'quantity': '1', 'unit': 'teaspoon', 'name': 'salt'}]`。
3. **数据重塑与转换**：
    - 将 `parse_ingredients` 函数应用到 `ingredients` 列，生成一个新列 `parsed_ingredients`。
    - 使用 Pandas 的方法将 `parsed_ingredients` 列展开，使得每一条配料信息都成为独立的一行，并包含 `recipe_name`, `quantity`, `unit`, `name` 这些列。
4. **数据分析**：
    - 找出在所有菜谱中，使用次数最多的 5 种配料 (ingredient `name`)。
    - 找出所有需要用到 `milk` 的菜谱名称。
"""

import pandas as pd
import re

def parse_ingredients(df_for_process: pd.DataFrame):
    df_for_process['parsed_ingredients'] = df_for_process['ingredients'].apply(lambda x: x.split(';'))
    pattern = re.compile(
        r"""
        ^\s*  # 开头可能有的空格
        (\d+\s*\d*\/\d*|\d+\.\d+|\d+|a|an|some)\s+  # 数量（如 1, 1.5, 1/2, a, some）
        (\w+)\s+                                   # 单位（如 cup, tbsp）
        ([\w\s-]+)                                 # 食材名称（允许空格和连字符）
        \s*$                                       # 结尾可能有的空格
        """,
        re.VERBOSE
    )
    parsed_data = []
    for ingredients_list in df_for_process['parsed_ingredients']:
        row_results = []
        for ingredient in ingredients_list:
            match = pattern.search(ingredient.strip())
            if match:
                row_results.append({
                    'quantity': match.group(1).strip(),
                    'unit': match.group(2).strip(),
                    'name': match.group(3).strip()
                })
            else:
                row_results.append({
                    'quantity': None,
                    'unit': None,
                    'name': ingredient.strip()
                })
        parsed_data.append(row_results)
    df_for_process['parsed_ingredients'] = parsed_data
    print(df_for_process['parsed_ingredients'])

if __name__ == '__main__':
    data = {
        'recipe_name': ['Classic Pancakes', 'Simple Omelette', 'Chocolate Cake'],
        'ingredients': [
            '1 1/2 cups all-purpose flour; 2 tablespoons sugar; 1 teaspoon baking powder; 1/2 tsp salt; 1 1/4 cups milk; 1 large egg',
            '2 large eggs; 2 tbsp milk; a pinch of salt; black pepper to taste',
            '2 cups sugar; 1 3/4 cups all-purpose flour; 3/4 cup cocoa powder; 1.5 teaspoons baking soda; 2 large eggs; 1 cup milk'
        ]
    }

    df = pd.DataFrame(data)
    parse_ingredients(df)



