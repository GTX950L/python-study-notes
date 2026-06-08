"""
异常处理学习笔记 — try / except / else / finally / raise
==================================================
为什么需要异常处理？
  没有异常处理时，程序一出错就直接崩溃（报错 + 退出）
  有了异常处理，程序可以「优雅地」处理错误、记录日志、继续运行

运行本文件：python basics/exception_handling.py
"""

# ==================== 1. 最基本的 try/except ====================

print("=== 1. 基本 try/except ===")

# 没有异常处理的写法（程序会崩溃）
# print(int("abc"))  # ValueError: invalid literal for int() with base 10

# 有异常处理的写法（程序不会崩溃）
try:
    result = int("abc")
    print(f"转换结果：{result}")
except ValueError:
    print("  ⚠️ 转换失败：'abc' 不是合法的数字字符串")
    result = None  # 给一个默认值

print(f"程序继续运行，result = {result}")


# ==================== 2. 捕获多种异常 ====================

print("\n=== 2. 捕获多种异常 ===")

# 方式一：一个 except 捕获多种异常
try:
    num = int("10")
    result = 100 / num
    my_list = [1, 2, 3]
    print(my_list[5])  # 这里会触发 IndexError
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"  ⚠️ 出错了：{type(e).__name__}: {e}")

# 方式二：分别处理不同异常（更精细）
print("\n--- 分别处理不同异常 ---")
try:
    # 试试把下面这行改成 num = 0 看看效果
    num = int("10")
    result = 100 / num
except ValueError:
    print("  ⚠️ 数字格式错误")
except ZeroDivisionError:
    print("  ⚠️ 不能除以零")
else:
    # else 块：只有当 try 块【没有发生任何异常】时才执行
    print(f"  ✅ 计算成功：100 / {num} = {result}")
finally:
    # finally 块：【无论是否发生异常】都会执行
    # 常用于清理资源（关闭文件、关闭数据库连接等）
    print("  📛 finally：清理工作完成")


# ==================== 3. else 和 finally 详解 ====================

print("\n=== 3. else / finally 详解 ===")

def safe_divide(a, b):
    """安全地做除法"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("  ⚠️ 错误：除数不能为零")
        return None
    else:
        # 没有异常才执行（可以放「正常逻辑」）
        print(f"  ✅ 除法成功：{a} / {b} = {result}")
        return result
    finally:
        # 无论结果如何都执行（清理逻辑）
        print("  📛 finally：除法操作结束")

safe_divide(100, 2)
print("---")
safe_divide(100, 0)


# ==================== 4. 主动抛出异常 raise ====================

print("\n=== 4. raise 主动抛出异常 ===")

def set_age(age):
    """设置年龄 — 用 raise 做参数校验"""
    if not isinstance(age, int):
        raise TypeError(f"age 必须是整数，你传了 {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age 必须在 0~150 之间，你传了 {age}")
    print(f"  ✅ 年龄设置为 {age}")
    return age

# 正常调用
try:
    set_age(25)
except (TypeError, ValueError) as e:
    print(f"  ⚠️ {e}")

# 异常调用
try:
    set_age(-5)
except (TypeError, ValueError) as e:
    print(f"  ⚠️ {e}")

try:
    set_age("二十五")
except (TypeError, ValueError) as e:
    print(f"  ⚠️ {e}")


# ==================== 5. 自定义异常类 ====================

print("\n=== 5. 自定义异常类 ===")

class DeviceError(Exception):
    """设备相关异常的基类"""
    pass

class DeviceOfflineError(DeviceError):
    """设备离线异常"""
    def __init__(self, device_id: str):
        self.device_id = device_id
        super().__init__(f"设备 {device_id} 当前离线，无法执行操作")

class MaintenanceError(DeviceError):
    """设备保养异常"""
    def __init__(self, device_id: str, reason: str):
        self.device_id = device_id
        super().__init__(f"设备 {device_id} 保养失败：{reason}")

def check_device_status(device_id: str, is_online: bool, needs_maintenance: bool):
    """检查设备状态 — 用自定义异常"""
    if not is_online:
        raise DeviceOfflineError(device_id)
    if needs_maintenance:
        raise MaintenanceError(device_id, "已超过90天未保养")

# 测试自定义异常
print("--- 测试1：设备离线 ---")
try:
    check_device_status("PL-8222-A", is_online=False, needs_maintenance=False)
except DeviceOfflineError as e:
    print(f"  ⚠️ 捕获到设备离线异常：{e}")
except MaintenanceError as e:
    print(f"  ⚠️ 捕获到保养异常：{e}")
except DeviceError as e:
    print(f"  ⚠️ 捕获到设备异常：{e}")

print("\n--- 测试2：需要保养 ---")
try:
    check_device_status("PL-8222-A", is_online=True, needs_maintenance=True)
except DeviceError as e:
    print(f"  ⚠️ {e}")


# ==================== 6. 实际场景：文件读取保护 ====================

print("\n=== 6. 实际场景：安全地读取文件 ===")

def read_file_safe(filepath: str) -> str | None:
    """
    安全地读取文件内容
    返回文件内容（字符串），失败返回 None
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"  ✅ 文件读取成功：{filepath}（{len(content)} 字符）")
        return content
    except FileNotFoundError:
        print(f"  ⚠️ 文件不存在：{filepath}")
    except PermissionError:
        print(f"  ⚠️ 没有权限读取：{filepath}")
    except UnicodeDecodeError as e:
        print(f"  ⚠️ 文件编码错误：{e}")
    except Exception as e:
        # 兜底：捕获所有其他异常（不建议在生产代码中滥用）
        print(f"  ⚠️ 未知错误：{type(e).__name__}: {e}")
    return None

# 测试
read_file_safe("README.md")       # 应该成功
read_file_safe("不存在的文件.txt")  # 应该捕获 FileNotFoundError


# ==================== 7. 总结：什么时候用异常处理 ====================

print("\n=== 7. 总结 ===")
print("""
✅ 用异常处理的场景：
  1. 调用可能失败的外部资源（文件、网络、数据库）
  2. 用户输入校验（转 int、读取配置）
  3. 除法、索引访问等「可能出错」的操作
  4. 需要「即使出错也不能崩溃」的关键逻辑

❌ 不要用异常处理代替正常逻辑：
  # 不好的写法：
  try:
      item = my_list[index]
  except IndexError:
      item = None

  # 更好的写法：
  item = my_list[index] if index < len(my_list) else None

✅ 异常处理最佳实践：
  - 捕获【具体的】异常，不要直接 except Exception
  - 自定义异常让错误语义更清晰
  - finally 用来做清理（关闭文件/连接）
  - raise 可以带上原始异常（raise NewError() from original_error）
""")
