import csv
import re

# 定义正则表达式
pattern = re.compile(r',\d+')

# 打开CSV文件
with open('train.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # 用于跟踪行号的变量
    line_number = 1

    # 遍历每一行
    for row in csvreader:
        # 将列表转换为字符串
        str_row = ','.join(row)

        # 如果该行不匹配正则表达式，打印该行及其行号
        if not pattern.search(str_row):
            print(f"Line {line_number}: {str_row}")

        # 更新行号
        line_number += 1