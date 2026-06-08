"""
模块与包学习笔记 — import / from...import / __init__.py / pip
==================================================
为什么要学模块？
  把代码分散到多个文件（模块），主程序更干净
  复用别人的代码（标准库、第三方包），不用重复造轮子

运行本文件：python basics/modules.py
"""

# ==================== 1. 导入模块的四种方式 ====================

print("=== 1. 导入模块的四种方式 ===\n")

# 方式一：import 模块名（最常用，推荐）
# 使用时需要加「模块名.」
import math
print(f"  math.pi = {math.pi}")
print(f"  math.sqrt(16) = {math.sqrt(16)}")

# 方式二：from 模块 import 名字（直接拿，不用加前缀）
# ⚠️ 注意：如果本地有同名变量会冲突
from random import randint
print(f"  randint(1, 10) = {randint(1, 10)}")

# 方式三：import ... as ...（起别名，常用在长模块名）
import datetime as dt
now = dt.datetime.now()
print(f"  现在时间：{now.strftime('%Y-%m-%d %H:%M')}")

# 方式四：from ... import *（导入所有公开名字，⚠️ 不推荐）
# 会从 module 里把所有「不以下划线开头」的名字都导进来
# 问题：不知道哪些名字被导入了，容易命名冲突
# from math import *  # ← 不推荐这样写


# ==================== 2. 标准库常用模块 ====================

print("\n=== 2. 标准库常用模块 ===\n")

# math — 数学运算
print("--- math 模块 ---")
print(f"  向上取整 ceil(3.2) = {math.ceil(3.2)}")
print(f"  向下取整 floor(3.8) = {math.floor(3.8)}")
print(f"  幂运算 pow(2, 10) = {math.pow(2, 10)}")

# random — 随机数
from random import choice, shuffle
print("\n--- random 模块 ---")
my_list = [1, 2, 3, 4, 5]
shuffled = my_list.copy()
shuffle(shuffled)
print(f"  随机选一个：{choice(my_list)}")
print(f"  随机打乱：{shuffled}")

# os / pathlib — 文件路径操作（跨平台）
from pathlib import Path
print("\n--- pathlib 模块（推荐用这个，比 os.path 更现代）---")
p = Path("basics/hello_world.py")
print(f"  文件存在？{p.exists()}")
print(f"  文件名：{p.name}")
print(f"  后缀：{p.suffix}")

# datetime — 日期时间
from datetime import datetime, timedelta
print("\n--- datetime 模块 ---")
tomorrow = datetime.now() + timedelta(days=1)
print(f"  明天这个时候：{tomorrow.strftime('%Y-%m-%d %H:%M')}")

# json — JSON 读写（和字典互相转换）
import json
print("\n--- json 模块 ---")
data = {"name": "GTX950L", "level": "业余爱好者"}
json_str = json.dumps(data, ensure_ascii=False)
print(f"  字典 → JSON 字符串：{json_str}")
parsed = json.loads(json_str)
print(f"  JSON 字符串 → 字典：{parsed['name']}")


# ==================== 3. 创建自己的模块 ====================

print("\n=== 3. 创建自己的模块 ===")
print("""
假设项目结构是这样：

my_project/
├── main.py          # 主程序
├── utils.py         # 自己写的工具模块
└── calculators/
    ├── __init__.py  # 把文件夹变成「包」的关键文件
    ├── bmi.py       # 子模块：BMI 计算
    └── salary.py    # 子模块：薪资计算

在 main.py 里可以这样用：

  # 导入自己写的模块（和导入标准库完全一样）
  import utils
  from calculators.bmi import calculate_bmi

  result = calculate_bmi(70, 1.75)
  print(f"BMI = {result}")
""")

# 演示：动态创建一个「自己的模块」并导入
# 在实际项目中，你会手动创建 utils.py 文件，然后 import
print("  （在当前项目中，你可以创建 my_utils.py 然后 import my_utils）")


# ==================== 4. __init__.py 的作用 ====================

print("\n=== 4. __init__.py 的作用 ===")
print("""
__init__.py 做了两件事：

1. 标记这是一个「包」（package）而不是普通文件夹
   （Python 3.3+ 支持 namespace package，技术上可以没有 __init__.py，
   但实际项目中还是建议加上）

2. 在「包被导入」时自动执行（可以用来做初始化、统一导出）

例：calculators/__init__.py 内容：
---
# 在包级别统一导出，让外部调用更简洁
from .bmi import calculate_bmi
from .salary import calculate_salary

__all__ = ["calculate_bmi", "calculate_salary"]
---

然后外部就可以：
  from calculators import calculate_bmi   # ← 不需要知道 bmi.py 的存在
""")


# ==================== 5. 安装和使用第三方包 ====================

print("\n=== 5. 安装和使用第三方包（pip）===")
print("""
# 安装包（在命令行/终端里执行，不是在 Python 里）
pip install requests
pip install pandas
pip install matplotlib

# 安装指定版本
pip install requests==2.31.0

# 查看已安装的包
pip list

# 从 requirements.txt 批量安装（项目标配）
pip install -r requirements.txt

# 在 Python 里使用安装的包
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
""")

# 演示：尝试导入 requests（如果装了的话）
try:
    import requests
    print("  ✅ requests 已安装")
    print(f"    版本：{requests.__version__}")
except ImportError:
    print("  ⚠️ requests 未安装，运行：pip install requests")


# ==================== 6. if __name__ == "__main__" 是什么 ====================

print("\n=== 6. if __name__ == \"__main__\" ===")
print("""
这是一个非常常见的 Python 惯用法。

意思：
  「如果当前文件是被【直接运行】的，才执行下面的代码」
  「如果被 import 的，不执行」（因为作为模块导入时，通常只想要里面的函数/类，不想跑测试代码）

例：my_module.py
---
def my_function():
    return "hello"

# 这段只有在「python my_module.py」直接运行时才会执行
# 如果是「import my_module」，这段不会执行
if __name__ == "__main__":
    print("模块直接运行，执行测试")
    print(my_function())
---

好处：
  1. 模块里的函数可以被其他文件 import 复用
  2. 模块自己也可以直接运行测试
""")


# ==================== 7. 总结 ====================

print("\n=== 7. 总结 ===")
print("""
✅ import 的四种方式：
  1. import math                              → 用 math.pi
  2. from random import randint                → 直接用 randint()
  3. import datetime as dt                   → 用 dt.datetime.now()
  4. from math import *                      → ❌ 不推荐

✅ 标准库值得先熟悉的：
  - math / random   → 数学和随机数
  - pathlib          → 文件路径（比 os.path 好用）
  - datetime         → 日期时间处理
  - json             → JSON 和字典互转
  - os / sys         → 系统相关（进阶再用）

✅ 第三方包管理：
  pip install 包名
  import 包名

✅ 自己的项目结构：
  my_project/
  ├── main.py           # 入口
  ├── utils/            # 自己的工具包
  │   ├── __init__.py
  │   └── helpers.py
  └── requirements.txt  # 依赖清单
""")
