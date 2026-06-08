"""
OOP 学习笔记 ③ — 封装（Encapsulation）
==========================================
核心问题：封装是什么？

封装 = 把「内部细节」藏起来，只暴露「安全的接口」

为什么要封装？
  1. 防止外部乱改内部数据（比如把年龄设为 -5）
  2. 内部实现可以随时改，不影响外部调用者
  3. 代码更可控、更好维护

Python 里没有真正的「私有」，靠「约定」来实现封装：
  - 单下划线 _attr   → 「建议」外部不要直接访问（弱私有）
  - 双下划线 __attr  → 名称改写，外部更难直接访问（强私有）
  - @property        → 把方法变成「像属性一样访问」

运行：python oop/03_encapsulation.py
"""

# ==================== 1. 单下划线 _attr（约定上的私有）====================

print("=== 1. 单下划线 _attr（弱私有）===\n")

class Device:
    """
    单下划线开头：告诉别人「这是内部用的，别直接从外面访问」
    但不强制——你硬要访问也能访问到（Python 的哲学：成人之间互相信任）
    """

    def __init__(self, device_id: str, name: str):
        self.device_id = device_id
        self.name = name
        self._status = "正常"   # ← 单下划线：建议外部不要直接改
        self._maintenance_log = []  # ← 内部日志，不建议外部直接操作

    def set_status(self, new_status: str):
        """通过方法来改状态（可以加校验）"""
        valid = ["正常", "维修中", "停机"]
        if new_status not in valid:
            raise ValueError(f"无效状态：{new_status}，可选：{valid}")
        old = self._status
        self._status = new_status
        print(f"  ✅ 状态变更：{old} → {new_status}")

    def get_status(self):
        return self._status


dev = Device("PL-8222-A", "主电机")
dev.set_status("维修中")
print(f"  当前状态：{dev.get_status()}")

# 但「约定」不强制——你硬要直接改也能改（不推荐）
dev._status = "偷偷改的状态"  # ⚠️ 不推荐，但能跑
print(f"  ⚠️ 直接改了 _status：{dev._status}")


# ==================== 2. 双下划线 __attr（名称改写）====================

print("\n=== 2. 双下划线 __attr（强私有）===\n")

class Sensor:
    """
    双下划线开头：Python 会做「名称改写」（name mangling）
    外部访问 self.__calibration_data 会变成 self._Sensor__calibration_data
    直接访问 obj.__calibration_data 会报 AttributeError
    """

    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.__calibration_data = None  # ← 双下划线：外部无法直接访问
        self._raw_readings = []            # ← 单下划线：弱私有

    def calibrate(self, value: float):
        """校准 — 通过方法来修改私有属性"""
        if value < 0:
            raise ValueError("校准值不能为负")
        self.__calibration_data = value
        print(f"  ✅ 校准完成：{value}")

    def get_calibration(self):
        return self.__calibration_data


s = Sensor("TEMP-001")
s.calibrate(36.5)
print(f"  校准值：{s.get_calibration()}")

# 直接访问会报错（名称改写保护了它）
try:
    print(s.__calibration_data)
except AttributeError as e:
    print(f"  ⚠️ 无法直接访问 __calibration_data：{e}")

# 但「名称改写」不是真正的不可访问（还是能绕开，只是麻烦一点）
print(f"  （绕开名称改写访问）：{s._Sensor__calibration_data}")


# ==================== 3. @property — 最优雅的封装方式 ====================

print("\n=== 3. @property — 像访问属性一样调用方法 ===\n")

class Motor:
    """
    @property 让「方法」可以「像属性一样」访问：
      temp = motor.temperature   ← 看起来像访问属性
      实际上背后调用了 def temperature(self): ...

    好处：
      1. 外部调用更自然（不用写 motor.get_temperature()）
      2. 可以在「获取/设置」时加逻辑（校验、计算）
      3. 内部实现变了，外部调用代码不用改
    """

    def __init__(self, motor_id: str):
        self.motor_id = motor_id
        self._temperature = 25.0  # 内部温度值
        self._rpm = 0

    @property
    def temperature(self):
        """获取温度 — 像属性一样访问：motor.temperature"""
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        """设置温度 — 像属性一样赋值：motor.temperature = 80.0"""
        if value < -50 or value > 200:
            raise ValueError(f"温度 {value}°C 超出合理范围")
        old = self._temperature
        self._temperature = value
        print(f"  🌡️ 温度 {old}°C → {value}°C")

    @property
    def rpm(self):
        """转速 — 只读属性（没有 @rpm.setter）"""
        return self._rpm

    @rpm.setter
    def rpm(self, value: int):
        if value < 0:
            raise ValueError("转速不能为负")
        self._rpm = value
        print(f"  ⚙️ 转速设置为 {value} RPM")


m = Motor("M-001")
# 像属性一样用，但实际上背后调用了方法（有校验逻辑）
m.temperature = 85.0   # ← 调用 @temperature.setter
print(f"  当前温度：{m.temperature}°C")  # ← 调用 @property

m.rpm = 1500
print(f"  当前转速：{m.rpm} RPM")

# 尝试设非法值
try:
    m.temperature = 300.0
except ValueError as e:
    print(f"  ⚠️ {e}")


# ==================== 4. @property 的真实使用场景 ====================

print("\n=== 4. @property 真实场景：延迟计算 ===\n")

class MaintenanceReport:
    """
    场景：保养报告
    报告内容需要「从数据库加载」，但希望外部像访问属性一样用
    """

    def __init__(self, device_id: str):
        self.device_id = device_id
        self._cache = None  # 缓存：第一次加载后存起来

    @property
    def content(self):
        """懒加载：第一次访问时才去「加载」（模拟耗时操作）"""
        if self._cache is None:
            print("  📂 首次访问，正在加载报告内容...")
            # 模拟从数据库/文件加载
            self._cache = f"设备 {self.device_id} 的保养报告：\n  - 上次保养：2026-05-01\n  - 下次计划：2026-08-01"
        return self._cache


report = MaintenanceReport("PL-8222-A")
print(report.content)  # 第一次：加载
print("(再次访问，直接用缓存)")
print(report.content)  # 第二次：直接用缓存


# ==================== 5. 总结 ====================

print("\n=== 5. 总结 ===\n")
print("""
✅ 封装的三层防护：
  1. 公开属性（无下划线）    → 外部随意访问/修改
  2. 弱私有 _attr（单下划线）→ 建议不要直接访问（约定）
  3. 强私有 __attr（双下划线）→ 名称改写，外部难直接访问

✅ @property 是最好的封装工具：
  - 让方法「像属性一样」被访问（调用更自然）
  - 可以在 getter/setter 里加校验逻辑
  - 内部实现变了，外部代码不用改

✅ 什么时候用封装？
  - 属性需要校验（温度不能为负）→ 用 @setter
  - 属性是「算出来的」（不是存着的）→ 用 @property
  - 想隐藏内部实现细节 → 用 _ 或 __

⚠️ Python 的封装是「君子协定」：
  - 没有真正的私有，都能绕开
  - 但大家都遵守约定，所以够用了

下一篇：04_polymorphism.py — 多态（同一接口，不同表现）
""")
