"""
📈 数据可视化入门：matplotlib
============================
matplotlib 是 Python 最基础的绘图库，
虽然代码比 Excel 多一点，但自由度极高。
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置中文字体（Windows 默认支持 SimHei）
plt.rcParams["font.sans-serif"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# ============================================================
# 模拟生产数据
# ============================================================

产线数据 = pd.DataFrame({
    "日期":    ["06-01", "06-02", "06-03", "06-04", "06-05"],
    "8222产量": [3200, 3350, 3280, 3420, 3380],
    "9610产量": [5200, 5150, 5300, 5250, 5180],
    "8222合格": [3180, 3330, 3260, 3400, 3360],
    "9610合格": [5180, 5120, 5280, 5230, 5160],
})

设备类型 = pd.DataFrame({
    "设备类型": ["电阻焊", "注水", "扩孔", "测温", "氮气柜"],
    "平均产量": [3100, 4200, 3600, 5100, 2800],
    "设备数":   [8, 6, 4, 5, 3],
})

合格率数据 = pd.DataFrame({
    "日期":   ["06-01", "06-02", "06-03", "06-04", "06-05"],
    "8222合格率": [99.4, 99.4, 99.4, 99.4, 99.4],
    "9610合格率": [99.6, 99.4, 99.6, 99.6, 99.4],
})

# ============================================================
# 一、折线图 — 趋势变化
# ============================================================

print("📈 生成折线图：8222 / 9610 日产量趋势")
plt.figure(figsize=(10, 5))
plt.plot(产线数据["日期"], 产线数据["8222产量"], marker="o", label="8222 产量")
plt.plot(产线数据["日期"], 产线数据["9610产量"], marker="s", label="9610 产量")
plt.title("日产量趋势")
plt.xlabel("日期")
plt.ylabel("产量（台）")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("折线图_日产量趋势.png", dpi=150)
plt.close()
print("  ✅ 已保存为 折线图_日产量趋势.png\n")

# ============================================================
# 二、柱状图 — 分类对比
# ============================================================

print("📊 生成柱状图：各设备类型平均产量")
plt.figure(figsize=(10, 5))
x = range(len(设备类型["设备类型"]))
plt.bar(x, 设备类型["平均产量"], color=["#58a6ff", "#7ee787", "#f0883e", "#ff7b72", "#bc8cff"])
plt.xticks(x, 设备类型["设备类型"])
plt.title("各设备类型平均产量")
plt.ylabel("平均产量（台）")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
for i, v in enumerate(设备类型["平均产量"]):
    plt.text(i, v + 50, str(v), ha="center")
plt.tight_layout()
plt.savefig("柱状图_设备类型产量.png", dpi=150)
plt.close()
print("  ✅ 已保存为 柱状图_设备类型产量.png\n")

# ============================================================
# 三、饼图 — 占比分布
# ============================================================

print("🥧 生成饼图：设备类型占比")
plt.figure(figsize=(7, 7))
plt.pie(
    设备类型["设备数"],
    labels=设备类型["设备类型"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#58a6ff", "#7ee787", "#f0883e", "#ff7b72", "#bc8cff"],
)
plt.title("设备类型占比")
plt.tight_layout()
plt.savefig("饼图_设备类型占比.png", dpi=150)
plt.close()
print("  ✅ 已保存为 饼图_设备类型占比.png\n")

# ============================================================
# 四、双轴图 — 产量 + 合格率
# ============================================================

print("📊 生成双轴图：产量 + 合格率")
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(合格率数据["日期"], 产线数据["8222产量"], alpha=0.6, label="8222 产量", color="#58a6ff")
ax1.set_ylabel("产量（台）", color="#58a6ff")
ax1.tick_params(axis="y", labelcolor="#58a6ff")

ax2 = ax1.twinx()
ax2.plot(合格率数据["日期"], 合格率数据["8222合格率"], marker="o", color="#7ee787", label="合格率")
ax2.set_ylabel("合格率（%）", color="#7ee787")
ax2.tick_params(axis="y", labelcolor="#7ee787")
ax2.set_ylim(98, 101)

plt.tight_layout()
plt.savefig("双轴图_产量与合格率.png", dpi=150)
plt.close()
print("  ✅ 已保存为 双轴图_产量与合格率.png\n")

print("=" * 50)
print("💡 关键要点：")
print("  - plt.figure(figsize=) 设置画布大小")
print("  - plt.plot() 折线图 / plt.bar() 柱状图 / plt.pie() 饼图")
print("  - plt.xlabel / ylabel / title 设置标签")
print("  - plt.legend() 显示图例")
print("  - plt.savefig() 保存为图片（dpi=150 够用）")
print("  - plt.twinx() 创建双 Y 轴")
print("  - plt.rcParams 设置中文字体，避免乱码")
print("  - plt.close() 用完就关，避免内存泄漏")
