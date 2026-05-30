"""
循环
重复执行一段代码，直到满足某个条件。
关键词：for、while
"""

# ---- for 循环：遍历序列 ----
print("=== 遍历列表 ===")
水果列表 = ["苹果", "香蕉", "橘子", "葡萄"]
for 水果 in 水果列表:
    print(f"我喜欢吃{水果}")

# ---- range()：生成数字序列 ----
print("\n=== range 用法 ===")
for i in range(5):          # 0 到 4
    print(f"第{i}次")

print()
for i in range(1, 6):       # 1 到 5
    print(f"第{i}次")

print()
for i in range(0, 10, 2):   # 步长为 2
    print(i, end=" ")       # end=" " 表示不换行
print()

# ---- while 循环：条件成立就一直跑 ----
print("\n=== 倒计时 ===")
倒计时 = 5
while 倒计时 > 0:
    print(f"还剩 {倒计时} 秒...")
    倒计时 -= 1             # 每次减 1，很重要！不然会死循环
print("发射！🚀")

# ---- break：提前退出循环 ----
print("\n=== break 示例 ===")
for i in range(10):
    if i == 5:
        print("到 5 了，不找了！")
        break               # 直接跳出循环
    print(f"当前数字：{i}")

# ---- continue：跳过本次循环 ----
print("\n=== continue 示例 ===")
for i in range(10):
    if i % 2 == 0:          # 如果是偶数
        continue             # 跳过，不打印
    print(f"奇数：{i}")

# ---- 练一练：九九乘法表 ----
print("\n=== 九九乘法表 ===")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}\t", end="")
    print()                  # 换行
