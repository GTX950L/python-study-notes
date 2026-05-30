"""
文件读写
把数据保存到文件中，或者从文件中读取数据。
"""

# ---- 写入文件 ----
print("=== 写入文件 ===")
with open("日记.txt", "w", encoding="utf-8") as 文件:
    文件.write("2024年6月1日 晴\n")
    文件.write("今天开始学 Python 的文件操作。\n")
    文件.write("感觉挺有意思的！\n")
print("已写入 '日记.txt'")

# ---- 追加内容 ----
with open("日记.txt", "a", encoding="utf-8") as 文件:
    文件.write("又学了一招：追加模式。\n")
print("已追加内容")

# ---- 读取整个文件 ----
print("\n=== 读取全部内容 ===")
with open("日记.txt", "r", encoding="utf-8") as 文件:
    内容 = 文件.read()
    print(内容)

# ---- 逐行读取 ----
print("=== 逐行读取 ===")
with open("日记.txt", "r", encoding="utf-8") as 文件:
    for 行号, 行 in enumerate(文件, 1):
        print(f"第{行号}行：{行.strip()}")

# ---- 读取所有行到列表 ----
print("\n=== 读取到列表 ===")
with open("日记.txt", "r", encoding="utf-8") as 文件:
    所有行 = 文件.readlines()
    print(f"共 {len(所有行)} 行")
    print(f"第一行：{所有行[0].strip()}")

# ---- 写入 CSV 格式 ----
print("\n=== CSV 写入 ===")
import csv

数据 = [
    ["姓名", "年龄", "城市"],
    ["张三", "25", "深圳"],
    ["李四", "30", "北京"],
    ["王五", "28", "上海"],
]

with open("用户.csv", "w", encoding="utf-8-sig", newline="") as 文件:
    写入器 = csv.writer(文件)
    写入器.writerows(数据)
print("已写入 '用户.csv'")

# ---- 读取 CSV ----
print("\n=== CSV 读取 ===")
with open("用户.csv", "r", encoding="utf-8-sig") as 文件:
    读取器 = csv.reader(文件)
    for 行 in 读取器:
        print(" | ".join(行))

# ---- 清理临时文件 ----
import os
os.remove("日记.txt")
os.remove("用户.csv")
print("\n临时文件已清理")
