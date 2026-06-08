"""
OOP 学习笔记 ⑤ — 类方法 / 静态方法 / 抽象类（进阶）
==================================================
前面四篇讲了：类与对象、继承、封装、多态
这一篇讲三个「进阶工具」：

  @classmethod — 类方法：第一个参数是「类本身」
  @staticmethod — 静态方法：跟类/对象都没啥关系，只是「归在一起」
  abc 模块    — 抽象基类：强制子类实现某些方法

运行：python oop/05_advanced.py
"""

# ==================== 1. @classmethod — 类方法 ====================

print("=== 1. @classmethod ===\n")

"""
普通方法（实例方法）：第一个参数是 self（对象本身）
类方法：第一个参数是 cls（类本身），可以访问/修改「类属性」

什么时候用 @classmethod？
  1. 工厂方法 — 用不同方式创建对象
  2. 操作「类级别」的数据（比如计数器）
  3. 继承场景下，cls() 会自动用「正确的子类」
"""

class Device:
    """设备类 — 演示 @classmethod"""

    device_count = 0  # 类属性：所有对象共享

    def __init__(self, device_id: str, name: str):
        self.device_id = device_id
        self.name = name
        Device.device_count += 1  # 修改类属性

    @classmethod
    def from_dict(cls, data: dict):
        """
        工厂方法：从字典创建 Device 对象
        cls 就是「当前类」（Device 或其子类）
        """
        return cls(
            device_id=data["device_id"],
            name=data["name"]
        )

    @classmethod
    def get_count(cls) -> int:
        """获取设备总数 — 通过 cls 访问类属性"""
        return cls.device_count


# 用法一：工厂方法（从字典创建）
data = {"device_id": "PL-001", "name": "主电机"}
dev = Device.from_dict(data)  # ← 不用写 Device()，用类方法创建
print(f"  从字典创建：{dev.device_id} - {dev.name}")

# 用法二：访问类级别数据
print(f"  设备总数：{Device.get_count()}")

# 用法三：继承场景（cls 会自动变成子类）
class ProductionLineDevice(Device):
    pass

data2 = {"device_id": "PL-002", "name": "产线电机"}
dev2 = ProductionLineDevice.from_dict(data2)  # cls = ProductionLineDevice
print(f"  子类工厂：{type(dev2).__name__}")  # ProductionLineDevice


# ==================== 2. @staticmethod — 静态方法 ====================

print("\n=== 2. @staticmethod ===\n")

"""
静态方法：
  - 没有 self，也没有 cls
  - 跟类/对象都没啥关系
  - 只是「逻辑上属于这个类」，归在一起方便管理

什么时候用 @staticmethod？
  1. 工具函数，但和这个类「语义相关」
  2. 不需要访问实例属性（self.xxx）或类属性（cls.xxx）
"""

class MathUtils:
    """数学工具 — 演示 @staticmethod"""

    @staticmethod
    def add(a: int, b: int) -> int:
        """加法 — 跟 MathUtils 这个类本身没关系，只是「归在一起」"""
        return a + b

    @staticmethod
    def is_even(n: int) -> bool:
        """判断偶数"""
        return n % 2 == 0


# 用法：可以直接用「类名.方法()」调用，不用创建对象
print(f"  MathUtils.add(3, 5) = {MathUtils.add(3, 5)}")
print(f"  MathUtils.is_even(4) = {MathUtils.is_even(4)}")

# 也可以从对象调用（但没必要）
mu = MathUtils()
print(f"  mu.is_even(7) = {mu.is_even(7)}")


# ==================== 3. 真实场景：设备 ID 生成器 ====================

print("\n=== 3. 真实场景：设备 ID 生成器 ===\n")

class DeviceIDGenerator:
    """设备 ID 生成器 — 用 @staticmethod 放工具函数"""

    @staticmethod
    def generate_production_line_id(line_name: str, index: int) -> str:
        """生成产线设备 ID：PL-8222-001"""
        return f"PL-{line_name}-{index:03d}"

    @staticmethod
    def generate_inspection_id(device_type: str, index: int) -> str:
        """生成检测设备 ID：IT-TEMP-001"""
        type_code = {
            "温度": "TEMP",
            "电阻": "RES",
            "压力": "PRES",
        }.get(device_type, "UNKN")
        return f"IT-{type_code}-{index:03d}"

    @staticmethod
    def parse_device_id(device_id: str) -> dict:
        """解析设备 ID，返回信息字典"""
        parts = device_id.split("-")
        if len(parts) >= 3:
            return {"prefix": parts[0], "line": parts[1], "index": parts[2]}
        return {"error": "无效 ID 格式"}


# 测试
id1 = DeviceIDGenerator.generate_production_line_id("8222", 1)
id2 = DeviceIDGenerator.generate_inspection_id("温度", 1)
print(f"  产线设备 ID：{id1}")
print(f"  检测设备 ID：{id2}")
print(f"  解析 ID：{DeviceIDGenerator.parse_device_id(id1)}")


# ==================== 4. abc 模块 — 抽象基类 ====================

print("\n=== 4. abc 抽象基类 ===\n")

"""
抽象基类（Abstract Base Class）：
  - 不能实例化（不能创建对象）
  - 子类【必须】实现 @abstractmethod 标注的方法，否则报错

什么时候用？
  1. 定义「接口规范」— 强制子类实现某些方法
  2. 防止误用 — 不能创建「不完整」的基类对象
"""

from abc import ABC, abstractmethod

class Device(ABC):
    """设备抽象基类 — 定义「所有设备必须有什么方法」"""

    def __init__(self, device_id: str):
        self.device_id = device_id

    @abstractmethod
    def perform_maintenance(self):
        """保养 — 子类【必须】实现"""
        pass

    @abstractmethod
    def show_status(self):
        """显示状态 — 子类【必须】实现"""
        pass

    def get_id(self) -> str:
        """普通方法 — 子类可以直接用，也可以重写"""
        return self.device_id


class ProductionLineDevice(Device):
    """产线设备 — 必须实现两个抽象方法，否则报错"""

    def perform_maintenance(self):
        return f"{self.device_id} 润滑传动部件 + 检查皮带"

    def show_status(self):
        return f"{self.device_id} 运行中"


class InspectionDevice(Device):
    """检测设备 — 也必须实现"""

    def perform_maintenance(self):
        return f"{self.device_id} 清洁传感器 + 校验零点"

    def show_status(self):
        return f"{self.device_id} 待机中"


# 测试：多态
devices = [ProductionLineDevice("PL-001"), InspectionDevice("IT-001")]
for d in devices:
    print(f"  {d.perform_maintenance()}")

# ❌ 如果有个类没实现抽象方法：
# class BadDevice(Device):
#     pass
# bd = BadDevice("PL-999")  # ← 这里会报 TypeError！


# ==================== 5. @classmethod vs @staticmethod 对比 ====================

print("\n=== 5. @classmethod vs @staticmethod 对比 ===\n")

print("""
  | 特性                | @classmethod       | @staticmethod     |
  |---------------------|--------------------|--------------------|
  | 第一个参数          | cls（类本身）     | 无                |
  | 能访问类属性？      | ✅ 能              | ❌ 不能           |
  | 能访问实例属性？    | ❌ 不能           | ❌ 不能           |
  | 继承时自动用子类？  | ✅ 能（cls 是子类）| ❌ 不能           |
  | 典型用途            | 工厂方法、类级别操作 | 工具函数           |

  简单记：
  - 方法里需要用到「类」→ @classmethod
  - 方法里啥都不需要    → @staticmethod
  - 方法里需要用到「对象」→ 普通实例方法（self）
""")


# ==================== 6. 总结 ====================

print("=== 6. 总结 ===\n")
print("""
✅ @classmethod：
  - 第一个参数是 cls（类本身）
  - 能访问/修改类属性
  - 典型用途：工厂方法（from_xxx）、类级别统计

✅ @staticmethod：
  - 没有 self，也没有 cls
  - 只是「语义上属于这个类」的工具函数
  - 典型用途：ID 生成器、格式转换、校验函数

✅ abc 抽象基类：
  - 不能实例化
  - 子类【必须】实现 @abstractmethod
  - 典型用途：定义接口规范、防止误用

✅ 三个都用在「面向对象设计」里：
  - @classmethod  → 类级别的操作用
  - @staticmethod  → 工具函数归位用
  - abc             → 强制接口规范用

📌 OOP 五篇全部完成！
  01_class_and_object.py  → 类与对象
  02_inheritance.py      → 继承
  03_encapsulation.py   → 封装
  04_polymorphism.py    → 多态
  05_advanced.py        → 类方法 / 静态方法 / 抽象类
""")
