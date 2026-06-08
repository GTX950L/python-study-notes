"""
OOP 学习笔记 ② — 继承（Inheritance）
========================================
核心问题：继承是什么？

继承 = 让「新类」自动获得「已有类」的属性和方法
已有类 = 父类（Parent / Base / Super class）
新类   = 子类（Child / Derived / Sub class）

为什么要继承？
  1. 代码复用 — 不用把父类的代码抄一遍
  2. 层次清晰 — 真实世界就是分层级的（设备 → 生产线设备 → 马达设备）
  3. 为多态打基础

运行：python oop/02_inheritance.py
"""

# ==================== 1. 最简单的继承 ====================

print("=== 1. 最简单的继承 ===\n")

class Animal:
    """父类：动物"""
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        """叫 — 父类不知道具体怎么叫，留给子类实现"""
        raise NotImplementedError("子类必须实现 speak() 方法")

    def breathe(self):
        """呼吸 — 所有动物都会，父类直接实现"""
        return f"{self.name} 在呼吸..."


class Dog(Animal):
    """子类：狗，继承自 Animal"""
    def speak(self):
        return f"{self.name} 说：汪汪！"


class Cat(Animal):
    """子类：猫，继承自 Animal"""
    def speak(self):
        return f"{self.name} 说：喵喵～"


# 测试
dog = Dog("阿黄")
cat = Cat("小黑")

print(f"  {dog.name} → {dog.speak()}")
print(f"  {cat.name} → {cat.speak()}")
print(f"  {dog.name} → {dog.breathe()}")  # 继承自父类的方法
print(f"  {cat.name} → {cat.breathe()}")  # 同上


# ==================== 2. super() — 调用父类的方法 ====================

print("\n=== 2. super() 调用父类构造方法 ===\n")

class Device:
    """设备基类"""
    def __init__(self, device_id: str, name: str, location: str):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.status = "正常"
        print(f"  Device 构造方法被调用：{device_id}")

    def show_status(self):
        print(f"  [{self.device_id}] {self.name} — 状态：{self.status}")


class ProductionLineDevice(Device):
    """生产线设备 — 在父类基础上新增产线相关属性"""

    def __init__(self, device_id: str, name: str, location: str, line_name: str):
        # super() = 调用父类的 __init__
        super().__init__(device_id, name, location)
        # 子类自己的属性
        self.line_name = line_name
        print(f"  ProductionLineDevice 构造方法被调用：{line_name}")

    # 重写（Override）父类方法
    def show_status(self):
        """重写：展示更详细的状态"""
        super().show_status()  # 先调用父类的版本
        print(f"    所属产线：{self.line_name}")  # 再追加子类的内容


# 测试
dev = ProductionLineDevice("PL-8222-A", "主电机", "8222车间", "8222除气线")
dev.show_status()


# ==================== 3. 方法重写（Override）====================

print("\n=== 3. 方法重写（Override）===\n")

# 上面 ProductionLineDevice.show_status() 已经是重写的例子
# 关键点：子类方法和父类「同名」，调用时优先用子类的版本

class InspectionDevice(Device):
    """检测设备 — 重写 show_status"""
    def __init__(self, device_id: str, name: str, location: str, accuracy: str):
        super().__init__(device_id, name, location)
        self.accuracy = accuracy

    def show_status(self):
        """完全重写，不调用父类版本"""
        print(f"  [检测设备] {self.name}")
        print(f"    精度：{self.accuracy}")
        print(f"    状态：{self.status}")


insp = InspectionDevice("IT-TEMP-01", "红外测温仪", "8222车间", "±0.5°C")
insp.show_status()

# 验证：isinstance() — 判断「是不是某类的对象」
print(f"\n  dev 是 Device 吗？{isinstance(dev, Device)}")           # True
print(f"  dev 是 ProductionLineDevice 吗？{isinstance(dev, ProductionLineDevice)}")  # True
print(f"  dev 是 InspectionDevice 吗？{isinstance(dev, InspectionDevice)}")  # False


# ==================== 4. 继承链 — 多层继承 ====================

print("\n=== 4. 多层继承 ===\n")

class A:
    def method_a(self):
        print("  A.method_a()")

class B(A):
    def method_b(self):
        print("  B.method_b()")

class C(B):
    def method_c(self):
        print("  C.method_c()")

# C 继承了 B，B 继承了 A，所以 C 能访问全部
c = C()
c.method_a()  # 来自 A
c.method_b()  # 来自 B
c.method_c()  # 来自 C


# ==================== 5. 总结 ====================

print("\n=== 5. 总结 ===\n")
print("""
✅ 继承语法：class 子类(父类):
✅ 子类自动获得父类的属性和方法（代码复用）
✅ super() 调用父类的构造方法或其他方法
✅ 方法重写（Override）：子类定义同名方法，覆盖父类版本
✅ isintance(obj, Class) 判断对象是否属于某类（含继承关系）

⚠️ 注意：
  - 不要滥用继承！「是一个（is-a）」关系才用继承
    正确：狗 是一个 动物 → 继承 ✅
    错误：狗 有一个 尾巴 → 应该用「组合」，不是继承 ❌

下一篇：03_encapsulation.py — 封装（私有属性 / @property）
""")
