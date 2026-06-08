"""
OOP 学习笔记 ④ — 多态（Polymorphism）
==========================================
核心问题：什么是多态？

「同一个接口，不同的表现」
→ 同样的方法名，不同对象执行不同的逻辑

为什么需要多态？
  1. 调用代码更统一（不用 if 判断类型）
  2. 新增类型时不用改原有代码（开闭原则）
  3. 真实世界就是多态的（同样是「叫」，狗和猫不一样）

运行：python oop/04_polymorphism.py
"""

# ==================== 1. 最简单的多态 ====================

print("=== 1. 最简单的多态 ===\n")

class Dog:
    def speak(self):
        return "汪汪！"

class Cat:
    def speak(self):
        return "喵喵～"

class Duck:
    def speak(self):
        return "嘎嘎！"

# 多态的关键：不关心「是什么类型」，只关心「有没有 speak() 方法」
def make_animal_speak(animal):
    """不管传进来什么动物，只要它有 speak() 就能叫"""
    print(f"  {animal.speak()}")

# 同一个函数，不同表现
zoo = [Dog(), Cat(), Duck()]
for animal in zoo:
    make_animal_speak(animal)


# ==================== 2. 继承 + 多态（更常见）====================

print("\n=== 2. 继承 + 多态 ===\n")

class Device:
    """设备基类 — 定义「接口」（抽象方法）"""
    def __init__(self, device_id: str, name: str):
        self.device_id = device_id
        self.name = name

    def perform_maintenance(self):
        """保养 — 基类不实现，留给子类"""
        raise NotImplementedError("子类必须实现 perform_maintenance()")

    def show_status(self):
        raise NotImplementedError("子类必须实现 show_status()")


class ProductionLineDevice(Device):
    """生产线设备 — 保养方式一"""
    def perform_maintenance(self):
        return f"  🏭 {self.name}：润滑传动部件 + 检查皮带张力"

    def show_status(self):
        return f"  📊 产线设备 [{self.device_id}] {self.name} — 运行中"


class InspectionDevice(Device):
    """检测设备 — 保养方式二（完全不同）"""
    def perform_maintenance(self):
        return f"  🔬 {self.name}：清洁传感器 + 校验零点"

    def show_status(self):
        return f"  📊 检测设备 [{self.device_id}] {self.name} — 待机中"


# 多态的威力：统一调用，不同表现
devices = [
    ProductionLineDevice("PL-8222-A", "8222线主电机"),
    ProductionLineDevice("PL-9610-B", "9610线主电机"),
    InspectionDevice("IT-TEMP-01", "红外测温仪"),
]

print("  --- 执行保养（多态）---")
for d in devices:
    # 同样是 perform_maintenance()，不同设备做不同的事
    print(d.perform_maintenance())

print("\n  --- 查看状态（多态）---")
for d in devices:
    print(d.show_status())


# ==================== 3. 不用多态的写法（对比）====================

print("\n=== 3. 对比：不用多态（❌ 不推荐）===\n")

def old_style_maintenance(device):
    """不用多态：需要用 if 判断类型"""
    from types import InstanceType
    # 判断类型再分别处理（新增类型就要改这个函数 ❌）
    if isinstance(device, ProductionLineDevice):
        print(f"  {device.name}：润滑 + 检查皮带")
    elif isinstance(device, InspectionDevice):
        print(f"  {device.name}：清洁传感器 + 校验")
    else:
        print(f"  ⚠️ 未知设备类型：{type(device).__name__}")

print("  ❌ 这种写法的问题：")
print("     1. 新增设备类型要改这个函数（违反开闭原则）")
print("     2. if 链越来越长，难维护")
print("  ✅ 用多态：新增类型不用改原有代码")


# ==================== 4. Python 的「鸭子类型」（Duck Typing）====================

print("\n=== 4. 鸭子类型（Duck Typing）===\n")

# Python 不要求严格的继承关系
# 「走起来像鸭子、叫起来像鸭子，那就是鸭子」

class Robot:
    """没有继承 Device，但有 speak() 方法"""
    def speak(self):
        return "我是机器人，哔哔哔！"

def make_speak(obj):
    """不检查类型，只检查「有没有 speak 方法」"""
    if hasattr(obj, "speak") and callable(getattr(obj, "speak")):
        print(f"  {obj.speak()}")
    else:
        print(f"  ⚠️ {obj} 不会叫")

# Dog/Cat/Robot 完全没有继承关系，但都能传进去
make_speak(Dog())
make_speak(Cat())
make_speak(Robot())  # ← 没继承 Animal，但有 speak() 就能用


# ==================== 5. abc 模块 — 强制子类实现方法 ====================

print("\n=== 5. abc 模块（强制多态接口）===\n")

from abc import ABC, abstractmethod

class Shape(ABC):
    """图形基类 — 用 @abstractmethod 强制子类实现"""

    @abstractmethod
    def area(self) -> float:
        """面积 — 子类【必须】实现"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """周长 — 子类【必须】实现"""
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


# 多态：统一调用 area()，不同图形算不同公式
shapes = [Rectangle(3, 4), Circle(5)]
for s in shapes:
    print(f"  {type(s).__name__}：面积={s.area():.2f}，周长={s.perimeter():.2f}")

# ❌ 如果子类没实现抽象方法，实例化时会报错
print("\n  ⚠️ 如果有个 BadShape(Shape) 没实现 area()，实例化时会报 TypeError")


# ==================== 6. 真实场景：设备数据导出 ====================

print("\n=== 6. 真实场景：多态导出数据 ===\n")

class CSVDExporter:
    """导出为 CSV"""
    def export(self, data):
        print(f"  📄 导出为 CSV 格式（{len(data)} 条记录）")

class ExcelExporter:
    """导出为 Excel"""
    def export(self, data):
        print(f"  📊 导出为 Excel 格式（{len(data)} 条记录）")

class PDFExporter:
    """导出为 PDF"""
    def export(self, data):
        print(f"  📕 导出为 PDF 格式（{len(data)} 条记录）")

def export_device_data(exporter, data):
    """多态：不管什么导出器，统一调用 export()"""
    exporter.export(data)

data = [{"id": "PL-001"}, {"id": "PL-002"}]
exporters = [CSVDExporter(), ExcelExporter(), PDFExporter()]
for e in exporters:
    export_device_data(e, data)


# ==================== 7. 总结 ====================

print("\n=== 7. 总结 ===\n")
print("""
✅ 多态 = 同一接口，不同表现
  speak() → 狗说"汪"，猫说"喵"

✅ 实现多态的三种方式：
  1. 继承 + 方法重写（最正式）
     class Dog(Animal): def speak(self): ...
  2. 鸭子类型（Python 特色，更灵活）
     if hasattr(obj, "speak"): obj.speak()
  3. abc 抽象基类（强制子类实现，最严格）
     @abstractmethod 标注的方法，子类必须实现

✅ 多态的好处：
  - 调用代码更简洁（不用 if 判断类型）
  - 新增类型不用改老代码（开闭原则）
  - 真实业务场景的天然映射

✅ 典型场景：
  - 设备多态：同样 perform_maintenance()，不同设备不同保养流程
  - 导出多态：同样 export()，导出不同格式
  - 支付方式：同样 pay()，微信/支付宝/银行卡不同实现

下一篇：05_advanced.py — 类方法 / 静态方法 / 抽象类
""")
