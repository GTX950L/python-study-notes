"""
📥 pandas 数据读取：Excel 和 CSV
=================================
最常见的数据源是 Excel 和 CSV 文件，
pandas 提供了简洁的读取接口。
"""

import pandas as pd

# ============================================================
# 一、读取 CSV
# ============================================================

# 基本读取
# df = pd.read_csv("数据文件.csv")

# 常用参数说明（这里用示例数据演示）
print("📄 CSV 读取常用参数：")
print("""
  pd.read_csv(
      "文件.csv",
      encoding="utf-8",        # 中文通常用 utf-8 或 gbk
      header=0,                # 第几行作为列名（0=第一行）
      usecols=["列A", "列B"],  # 只读取指定列
      nrows=100,               # 只读前 100 行（预览用）
      dtype={"列A": str},      # 指定列的数据类型
      parse_dates=["日期列"],  # 自动解析日期
  )
""")

# ============================================================
# 二、读取 Excel
# ============================================================

print("📗 Excel 读取常用参数：")
print("""
  pd.read_excel(
      "文件.xlsx",
      sheet_name="Sheet1",     # 指定工作表（可以是名称或索引）
      sheet_name=None,         # None = 读取所有 sheet，返回字典
      header=0,                # 第几行作为列名
      usecols="A:C",           # 只读取 A 到 C 列
      skiprows=3,              # 跳过前 3 行
      dtype={"编号": str},     # 指定列类型（避免科学计数法）
  )
""")

# ============================================================
# 三、写入文件
# ============================================================

print("💾 写入文件常用方法：")
print("""
  # 写入 CSV
  df.to_csv("输出.csv", index=False, encoding="utf-8-sig")
  
  # 写入 Excel（一个 sheet）
  df.to_excel("输出.xlsx", sheet_name="数据", index=False)
  
  # 写入 Excel（多个 sheet）
  with pd.ExcelWriter("输出.xlsx") as writer:
      df1.to_excel(writer, sheet_name="Sheet1", index=False)
      df2.to_excel(writer, sheet_name="Sheet2", index=False)
""")

# ============================================================
# 四、实战示例：读取并快速查看
# ============================================================

# 模拟制造测试数据
测试数据 = pd.DataFrame({
    "SN码":        [f"SN{1000+i:04d}" for i in range(5)],
    "测试日期":     ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03"],
    "电阻值(mΩ)":  [12.5, 13.1, 11.8, 12.9, 13.4],
    "注水量(ml)":  [500, 505, 498, 502, 501],
    "温度(℃)":     [25.3, 25.8, 26.1, 25.5, 25.9],
    "是否合格":     [True, True, False, True, False],
})

print("📊 数据预览（前3行）：")
print(测试数据.head(3))
print()

print("📊 数据概览：")
print(f"  总行数: {len(测试数据)}")
print(f"  总列数: {len(测试数据.columns)}")
print(f"  缺失值:\n{测试数据.isnull().sum()}")
print(f"\n📊 数值列统计：")
print(测试数据.describe())

print("\n" + "=" * 50)
print("💡 关键要点：")
print("  - read_csv() / read_excel() 是最常用的两个读取函数")
print("  - dtype 参数可以防止 SN 码被转成数字")
print("  - head() 快速预览、describe() 查看统计")
print("  - to_csv/index=False/utf-8-sig 避免中文乱码")
