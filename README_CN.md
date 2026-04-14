# StrPathlib

[![Python Version](https://img.shields.io/badge/python-3.4%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

**StrPathlib** 是对 Python 标准库 [`pathlib`](https://docs.python.org/zh-cn/3/library/pathlib.html) 的轻量级增强。它通过混入（mixin）类 `StrPath`，让所有路径对象（`Path`、`PosixPath`、`WindowsPath` 等）可以直接调用字符串的实例方法（如 `.upper()`、`.startswith()`、`.replace()`），而不必每次都手动转换为字符串。

## 特性

- ✅ **无缝集成**：`StrPathlib.Path` 完全兼容 `pathlib.Path`，原有路径方法全部保留。
- 🧵 **字符串即路径**：路径对象可直接使用 40+ 个字符串方法，如 `.split()`、`.find()`、`.strip()`。
- 🧩 **纯 Python 实现**：无需编译，复制即用。
- 📦 **轻量**：除了标准库外零依赖。
- 🔄 **完整导出**：重新导出了 `pathlib` 中的所有类（`Path`、`PosixPath`、`PurePath` 等），替换为增强版本。

## 安装

目前可以直接将 `strPathlib.py` 复制到你的项目中，或通过pypi安装：

```bash
pip install strpathlib
```

## 快速开始

```python
from strPathlib import Path

p = Path("hello/world.txt")

# 原有 pathlib 功能照常工作
print(p.parent)          # Path('hello')
print(p.suffix)          # '.txt'
print(p.exists())        # True / False

# 新增：直接调用字符串方法
print(p.upper())         # 'HELLO/WORLD.TXT'
print(p.find("world"))   # 6
print(p.startswith("hello"))  # True
print(p.replace(".txt", ".md"))  # 'hello/world.md'
```

你也可以导入其他增强类：

```python
from strPathlib import PosixPath, WindowsPath, PurePath

posix = PosixPath("/usr/bin/python3")
win = WindowsPath("C:/Users/Admin")
pure = PurePath("a/b/c")
```

## 核心原理

`StrPath` 是一个混入类，它实现了 `str` 的所有公有实例方法（约 45 个）。每个方法内部都通过 `self.as_posix()` 获取路径的字符串表示，然后委托给真正的字符串方法执行。

由于 `pathlib.Path` 及其子类已经提供了 `as_posix()` 方法（返回使用正斜杠的路径字符串），`StrPath` 可以安全地与它们一起使用。

通过多重继承，既保留了 `pathlib.Path` 的全部行为，又获得了字符串的方法集合。

> **注意**：字符串方法的返回值是普通的 Python 字符串（`str`）、布尔值或列表，**不会**返回新的 `Path` 对象。若需要继续使用路径功能，请重新包装：`Path(p.upper())`。

## 与标准 `pathlib` 的关系

本模块**并不修改**标准库中的 `pathlib`。它只是通过子类化创建了新的类，并将它们绑定到与 `pathlib` 相同的顶层名字上。因此，你可以安全地将其作为 drop-in replacement 使用：

```python
# 原代码
from pathlib import Path

# 改为
from strPathlib import Path
```

如果你同时需要标准库的原始类和增强类，可以这样导入：

```python
import pathlib
from strPathlib import Path as StrPath

original = pathlib.Path("a.txt")
enhanced = StrPath("a.txt")
```

## API 参考

### `StrPath`

混入基类，不应单独实例化。

**要求**：混入的目标类必须提供 `as_posix()` 方法（返回 `str`）。

### 增强的路径类

- `Path(pathlib.Path, StrPath)`
- `PosixPath(pathlib.PosixPath, StrPath)`
- `PurePath(pathlib.PurePath, StrPath)`
- `PurePosixPath(pathlib.PurePosixPath, StrPath)`
- `PureWindowsPath(pathlib.PureWindowsPath, StrPath)`
- `WindowsPath(pathlib.WindowsPath, StrPath)`

这些类的构造函数、属性和方法与对应的 `pathlib` 类完全一致。

## 注意事项

1. **平台相关**：字符串方法基于 `as_posix()` 的结果（始终使用正斜杠 `/`）。在 Windows 上，`as_posix()` 会将反斜杠转换为正斜杠。这对字符串操作通常无影响，但如果你依赖平台特定的分隔符，请注意。