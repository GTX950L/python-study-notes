"""
OOP 学习笔记 ① — 类与对象（Class & Object）
==========================================
核心问题：什么是类？什么是对象？

类（Class）   ：「模板」或「图纸」，定义了某类事物共有的属性和行为
对象（Object）：根据「模板」造出来的「具体东西」

类比：
  类 =「手机图纸」— 定义了手机有什么功能、什么样子
  对象 =「你手里那台手机」— 根据图纸造出来的具体一台

运行：python oop/01_class_and_object.py
"""

# ==================== 1. 定义一个最简单的类 ====================

print("=== 1. 定义类和创建对象 ===\n")

class Dog:
    """
    狗类 — 最基础的定义方式
    这个类现在只是个「图纸」，还没有「对象」
    """
    pass  # 暂时什么都不做，先搭个框架

# 根据「图纸」创建对象（实例化）
dog1 = Dog()
dog2 = Dog()

print(f"dog1 的类型：{type(dog1)}")   # <class '__main__.Dog'>
print(f"dog1 和 dog2 是同一个对象吗？{dog1 is dog2}")  # False（两个独立对象）

# ==================== 2. __init__ 构造方法 ====================

print("\n=== 2. __init__ 构造方法（创建对象时自动调用）===\n")

class Device:
    """
    设备类 — 用 __init__ 定义「创建设备时需要什么信息」

    __init__ 是「构造方法」：
      - 创建对象时【自动调用】
      - 用来做「初始化」（给属性赋初值）
      - self 代表「正在创建的这个对象本身」
    """

    def __init__(self, device_id: str, name: str, location: str):
        """
        device_id：设备编号
        name：设备名称
        location：所在位置
        self：Python 自动传入，代表「这个对象自己」
        """
        self.device_id = device_id   # 绑定到对象身上（属性）
        self.name = name
        self.location = location
        self.status = "正常"        # 默认值

    def show_info(self):
        """对象的方法（行为）"""
        print(f"  设备：{self.name}（{self.device_id}），状态：{self.status}")


# 创建两个设备对象
dev1 = Device("PL-8222-A", "8222线主电机", "8222车间")
dev2 = Device("IT-TEMP-01", "红外测温仪", "8222车间")

dev1.show_info()
dev2.show_info()

# 每个对象的属性是独立的
dev1.status = "维修中"
print(f"\n  修改后：dev1 状态 = {dev1.status}")
print(f"  dev2 状态（不受影响）= {dev2.status}")


# ==================== 3. 类属性和实例属性 ====================

print("\n=== 3. 类属性 vs 实例属性 ===\n")

class ProductionLine:
    """
    类属性：属于「类」本身的，所有对象共享同一份
    实例属性：属于「每个对象」的，互相独立
    """

    # 类属性（所有产线共享）
    factory_name = "武汉工厂"
    device_count = 0  # 用来统计创建了多少个对象

    def __init__(self, line_name: str):
        # 实例属性（每个对象自己的）
        self.line_name = line_name
        # 修改类属性（通过类名去改）
        ProductionLine.device_count += 1


line1 = ProductionLine("8222除气线")
line2 = ProductionLine("9610除气线")

print(f"  工厂名（类属性）：{ProductionLine.factory_name}")
print(f"  已创建产线数：{ProductionLine.device_count}")
print(f"  line1 的名字（实例属性）：{line1.line_name}")


# ==================== 4. 方法（对象的行为）====================

print("\n=== 4. 方法（对象能做什么）===\n")

class MaintenanceRecord:
    """保养记录类 — 演示方法的使用"""

    def __init__(self, device_id: str):
        self.device_id = device_id
        self.records = []  # 实例属性：这个设备的保养记录列表

    def add_record(self, content: str):
        """方法：给保养记录追加一条"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"[{timestamp}] {content}"
        self.records.append(entry)
        print(f"  ✅ 已添加记录：{content}")

    def show_records(self):
        """方法：展示所有记录"""
        if not self.records:
            print("  （暂无保养记录）")
            return
        print(f"  📋 {self.device_id} 的保养记录：")
        for i, r in enumerate(self.records, 1):
            print(f"    {i}. {r}")


mr = MaintenanceRecord("PL-8222-A")
mr.add_record("更换润滑油")
mr.add_record("检查皮带张力")
mr.show_records()


# ==================== 5. __str__ 和 __repr__（自定义打印输出）====================

print("\n=== 5. __str__ / __repr__（自定义 print 输出）===\n")

class Sensor:
    def __init__(self, sensor_id: str, sensor_type: str):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type

    def __str__(self):
        """str(obj) 或 print(obj) 时调用 — 给用户看的"""
        return f"传感器 [{self.sensor_id}]：{self.sensor_type}"

    def __repr__(self):
        """repr(obj) 时调用 — 给开发者看的（调试用）"""
        return f"Sensor(sensor_id='{self.sensor_id}', sensor_type='{self.sensor_type}')"


s = Sensor("TEMP-001", "温度传感器")
print(f"  print(s)  → {s}")     # 调用 __str__
print(f"  repr(s)  → {repr(s)}")  # 调用 __repr__


# ==================== 6. 总结 ====================

print("\n=== 6. 总结 ===\n")
print("""
✅ 类（Class）= 模板 / 图纸
✅ 对象（Object）= 根据模板造出来的具体实例
✅ __init__ = 构造方法，创建对象时自动调用
✅ self = 「这个对象自己」，方法里必须写
✅ 类属性 = 所有对象共享（通过 类名.属性 访问/修改）
✅ 实例属性 = 每个对象独立拥有
✅ 方法 = 对象能做的事（函数写在类里面就叫「方法」）
✅ __str__ / __repr__ = 自定义 print(obj) 的输出内容

下一篇：02_inheritance.py — 继承（子类复用父类代码）
""")
