import os
import yaml
import csv

# 设置项目目录
project_dir = 'projects'

# 初始化一个空列表来存储结果
results = []

# 遍历项目目录下的所有文件
for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.yaml'):
            # 构建文件的完整路径
            file_path = os.path.join(root, file)
            try:
                # 打开并读取YAML文件
                with open(file_path, 'r') as stream:
                    data = yaml.safe_load(stream)
                    # 提取所需的字段
                    main_repo = data.get('main_repo', 'N/A')
                    language = data.get('language', 'N/A')
                    # 将结果添加到列表中
                    results.append((file, main_repo, language))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# 打印结果或写入表格
# 将结果写入CSV文件
csv_file = 'results.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入标题行
    writer.writerow(['File', 'Main Repo', 'Language'])
    # 写入数据行
    for result in results:
        writer.writerow(result)

print(f"Results have been written to {csv_file}")