import pandas as pd

# 读取CSV文件
file_path = './data/train_dataset_1to100.csv'
df = pd.read_csv(file_path)

# 删除名为"id"的列
if 'id' in df.columns:
    df.drop(columns=['id'], inplace=True)

# 保存修改后的CSV文件
output_file_path = 'train_dataset_1to100_1.csv'
df.to_csv(output_file_path, index=False)

print("Successfully removed the 'id' column and saved the modified CSV file.")