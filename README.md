# StrPathlib

[![Python Version](https://img.shields.io/badge/python-3.4%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

**StrPathlib** is a lightweight enhancement to Python's standard [`pathlib`](https://docs.python.org/3/library/pathlib.html) library. By providing a mixin class `StrPath`, it enables all path objects (`Path`, `PosixPath`, `WindowsPath`, etc.) to directly invoke string instance methods (such as `.upper()`, `.startswith()`, `.replace()`), eliminating the need to manually convert to a string each time.  

[中文版](https://github.com/HZBHZB1234/strPathlib/blob/main/README_CN.md)

## Features

- ✅ **Seamless Integration**: `StrPathlib.Path` is fully compatible with `pathlib.Path`; all original path methods are preserved.
- 🧵 **Strings as Paths**: Path objects can directly use 40+ string methods, such as `.split()`, `.find()`, `.strip()`.
- 🧩 **Pure Python Implementation**: No compilation required – just copy and use.
- 📦 **Lightweight**: Zero dependencies outside the standard library.
- 🔄 **Complete Re-export**: Re-exports all classes from `pathlib` (`Path`, `PosixPath`, `PurePath`, etc.), replaced with enhanced versions.

## Installation

You can simply copy `strPathlib.py` into your project, or install via PyPI:

```bash
pip install strpathlib
```

## Quick Start

```python
from strPathlib import Path

p = Path("hello/world.txt")

# Original pathlib functionality works as usual
print(p.parent)          # Path('hello')
print(p.suffix)          # '.txt'
print(p.exists())        # True / False

# New: Directly call string methods
print(p.upper())         # 'HELLO/WORLD.TXT'
print(p.find("world"))   # 6
print(p.startswith("hello"))  # True
print(p.replace(".txt", ".md"))  # 'hello/world.md'
```

You can also import other enhanced classes:

```python
from strPathlib import PosixPath, WindowsPath, PurePath

posix = PosixPath("/usr/bin/python3")
win = WindowsPath("C:/Users/Admin")
pure = PurePath("a/b/c")
```

## Core Principles

`StrPath` is a mixin class that implements all public instance methods of `str` (approximately 45). Each method internally retrieves the string representation of the path via `self.as_posix()` and delegates to the actual string method.

Since `pathlib.Path` and its subclasses already provide the `as_posix()` method (which returns a path string using forward slashes), `StrPath` can safely be used with them.

Through multiple inheritance, the full behavior of `pathlib.Path` is preserved while gaining the set of string methods.

> **Note**: The return values of string methods are ordinary Python strings (`str`), booleans, or lists, **not** new `Path` objects. If you need to continue using path functionality, wrap the result again: `Path(p.upper())`.

## Relationship with Standard `pathlib`

This module **does not modify** the standard library's `pathlib`. It simply creates new classes via subclassing and binds them to the same top-level names as in `pathlib`. Therefore, it can safely be used as a drop-in replacement:

```python
# Original code
from pathlib import Path

# Change to
from strPathlib import Path
```

If you need both the standard library's original classes and the enhanced ones, you can import like this:

```python
import pathlib
from strPathlib import Path as StrPath

original = pathlib.Path("a.txt")
enhanced = StrPath("a.txt")
```

## API Reference

### `StrPath`

Mixin base class; should not be instantiated alone.

**Requirement**: The target class mixed in must provide an `as_posix()` method (returning a `str`).

### Enhanced Path Classes

- `Path(pathlib.Path, StrPath)`
- `PosixPath(pathlib.PosixPath, StrPath)`
- `PurePath(pathlib.PurePath, StrPath)`
- `PurePosixPath(pathlib.PurePosixPath, StrPath)`
- `PureWindowsPath(pathlib.PureWindowsPath, StrPath)`
- `WindowsPath(pathlib.WindowsPath, StrPath)`

The constructors, attributes, and methods of these classes are identical to the corresponding `pathlib` classes.

## Notes

1. **Platform Specifics**: String methods are based on the result of `as_posix()` (always using forward slashes `/`). On Windows, `as_posix()` converts backslashes to forward slashes. This usually does not affect string operations, but be aware if you rely on platform-specific separators.