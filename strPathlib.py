"""
strPathlib.py

This module provides StrPath, a mixin class that implements all public
instance methods of the built-in str type by delegating to the string
representation of a path (obtained via .as_posix()). It does not inherit
from pathlib.Path directly.

The module then re-exports the standard pathlib classes by subclassing
them together with StrPath, creating enhanced versions that behave like
ordinary strings in addition to their native path functionality:

    Path          (extends pathlib.Path)
    PosixPath     (extends pathlib.PosixPath)
    PurePath      (extends pathlib.PurePath)
    PurePosixPath (extends pathlib.PurePosixPath)
    PureWindowsPath (extends pathlib.PureWindowsPath)
    WindowsPath   (extends pathlib.WindowsPath)

All of these subclasses can be used wherever a path is expected, and they
also respond to all string methods (e.g., .upper(), .find(), .replace()).
When a string method is called, the path is first converted to a string
using self.as_posix(), and the corresponding str method is invoked. The
return value is whatever the str method normally returns (usually a string
or a bool), *not* another path instance.

Examples
--------
>>> p = Path("hello/world.txt")
>>> p
Path('hello/world.txt')
>>> p.upper()
'HELLO/WORLD.TXT'
>>> p.find("world")
6
>>> p.startswith("hello")
True
>>> (p / "subdir").parent
Path('hello')
"""

import pathlib
from pathlib import __all__ as _pathlib_all

__version__ = "0.1.0"

__all__ = _pathlib_all

class StrPath():
    """
    A mixin class that provides implementations for all public instance methods
    of the built-in str type. It does not inherit from pathlib.Path directly;
    instead, it is intended to be combined with a concrete Path class (e.g.,
    pathlib.Path) via multiple inheritance.

    The string methods delegate to the string representation of the path,
    obtained via the host class's `as_posix()` method. Therefore, any class
    that inherits from StrPath must provide an `as_posix()` method (which
    standard pathlib classes do). The return value of a string method is
    whatever the corresponding str method returns—typically a string or a
    bool—and *not* another path instance.

    This module exports several enhanced path classes (Path, PosixPath,
    PurePath, etc.) that are formed by subclassing the standard library's
    path classes together with StrPath. Those are the classes you should
    instantiate and use directly.
    """
    
    __slots__ = ()  # Keep memory footprint identical to Path.

    # ----------------------------------------------------------------------
    # String methods (manually implemented for IDE autocompletion)
    # ----------------------------------------------------------------------

    def capitalize(self) -> str:
        """
        Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.
        """
        return self.as_posix().capitalize()

    def casefold(self) -> str:
        """
        Return a casefolded copy of the string.

        Casefolding is similar to lowercasing but more aggressive because it is
        intended to remove all case distinctions in a string.
        """
        return self.as_posix().casefold()

    def center(self, width: int, fillchar: str = " ") -> str:
        """
        Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.as_posix().center(width, fillchar)

    def count(self, sub: str, start: int | None = None, end: int | None = None) -> int:
        """
        Return the number of non-overlapping occurrences of substring sub.

        Optional arguments start and end are interpreted as in slice notation.
        """
        return self.as_posix().count(sub, start, end)

    def encode(self, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        """
        Encode the string using the codec registered for encoding.

        encoding
          The encoding in which to encode the string.
        errors
          The error handling scheme to use for encoding errors.
          The default is 'strict' meaning that encoding errors raise a
          UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
          'xmlcharrefreplace' as well as any other name registered with
          codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return self.as_posix().encode(encoding, errors)

    def endswith(
        self, suffix: str | tuple[str, ...], start: int | None = None, end: int | None = None
    ) -> bool:
        """
        Return True if the string ends with the specified suffix, False otherwise.

        suffix can also be a tuple of suffixes to look for. With optional start, test
        beginning at that position. With optional end, stop comparing at that position.
        """
        return self.as_posix().endswith(suffix, start, end)

    def expandtabs(self, tabsize: int = 8) -> str:
        """
        Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return self.as_posix().expandtabs(tabsize)

    def find(self, sub: str, start: int | None = None, end: int | None = None) -> int:
        """
        Return the lowest index where substring sub is found.

        Return -1 if sub is not found. Optional arguments start and end are
        interpreted as in slice notation.
        """
        return self.as_posix().find(sub, start, end)

    def format(self, *args: object, **kwargs: object) -> str:
        """
        Return a formatted version of the string, using substitutions from args and kwargs.
        """
        return self.as_posix().format(*args, **kwargs)

    def format_map(self, mapping: dict[str, object]) -> str:
        """
        Return a formatted version of the string, using substitutions from mapping.
        """
        return self.as_posix().format_map(mapping)

    def index(self, sub: str, start: int | None = None, end: int | None = None) -> int:
        """
        Return the lowest index where substring sub is found.

        Raises ValueError if sub is not found. Optional arguments start and end are
        interpreted as in slice notation.
        """
        return self.as_posix().index(sub, start, end)

    def isalnum(self) -> bool:
        """
        Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character.
        """
        return self.as_posix().isalnum()

    def isalpha(self) -> bool:
        """
        Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character.
        """
        return self.as_posix().isalpha()

    def isascii(self) -> bool:
        """
        Return True if all characters in the string are ASCII, False otherwise.
        """
        return self.as_posix().isascii()

    def isdecimal(self) -> bool:
        """
        Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character.
        """
        return self.as_posix().isdecimal()

    def isdigit(self) -> bool:
        """
        Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character.
        """
        return self.as_posix().isdigit()

    def isidentifier(self) -> bool:
        """
        Return True if the string is a valid Python identifier, False otherwise.
        """
        return self.as_posix().isidentifier()

    def islower(self) -> bool:
        """
        Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character.
        """
        return self.as_posix().islower()

    def isnumeric(self) -> bool:
        """
        Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character.
        """
        return self.as_posix().isnumeric()

    def isprintable(self) -> bool:
        """
        Return True if the string is printable, False otherwise.

        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        return self.as_posix().isprintable()

    def isspace(self) -> bool:
        """
        Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character.
        """
        return self.as_posix().isspace()

    def istitle(self) -> bool:
        """
        Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only follow
        uncased characters and lowercase characters only cased ones.
        """
        return self.as_posix().istitle()

    def isupper(self) -> bool:
        """
        Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character.
        """
        return self.as_posix().isupper()

    def join(self, iterable: object) -> str:
        """
        Return a string which is the concatenation of the strings in iterable.

        The separator between elements is the string providing this method.
        """
        return self.as_posix().join(iterable)

    def ljust(self, width: int, fillchar: str = " ") -> str:
        """
        Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.as_posix().ljust(width, fillchar)

    def lower(self) -> str:
        """
        Return a copy of the string converted to lowercase.
        """
        return self.as_posix().lower()

    def lstrip(self, chars: str | None = None) -> str:
        """
        Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.as_posix().lstrip(chars)

    def maketrans(self, *args: object, **kwargs: object) -> dict[int, int | None]:
        """
        Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y.
        If there is a third argument, it must be a string, whose characters
        will be mapped to None in the result.
        """
        return self.as_posix().maketrans(*args, **kwargs)

    def partition(self, sep: str) -> tuple[str, str, str]:
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it. If the separator is not found, returns a 3-tuple
        containing the original string and two empty strings.
        """
        return self.as_posix().partition(sep)

    def removeprefix(self, prefix: str, /) -> str:
        """
        Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """
        return self.as_posix().removeprefix(prefix)

    def removesuffix(self, suffix: str, /) -> str:
        """
        Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original string.
        """
        return self.as_posix().removesuffix(suffix)

    def replace(self, old: str, new: str, count: int = -1) -> str:
        """
        Return a copy with all occurrences of substring old replaced by new.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        return self.as_posix().replace(old, new, count)

    def rfind(self, sub: str, start: int | None = None, end: int | None = None) -> int:
        """
        Return the highest index where substring sub is found.

        Return -1 if sub is not found. Optional arguments start and end are
        interpreted as in slice notation.
        """
        return self.as_posix().rfind(sub, start, end)

    def rindex(self, sub: str, start: int | None = None, end: int | None = None) -> int:
        """
        Return the highest index where substring sub is found.

        Raises ValueError if sub is not found. Optional arguments start and end are
        interpreted as in slice notation.
        """
        return self.as_posix().rindex(sub, start, end)

    def rjust(self, width: int, fillchar: str = " ") -> str:
        """
        Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        return self.as_posix().rjust(width, fillchar)

    def rpartition(self, sep: str) -> tuple[str, str, str]:
        """
        Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it. If the separator is not
        found, returns a 3-tuple containing two empty strings and the original string.
        """
        return self.as_posix().rpartition(sep)

    def rsplit(self, sep: str | None = None, maxsplit: int = -1) -> list[str]:
        """
        Return a list of the words in the string, using sep as the delimiter string.

        If maxsplit is given, at most maxsplit splits are done, the *rightmost* ones.
        If sep is not specified or is None, any whitespace string is a separator.
        """
        return self.as_posix().rsplit(sep, maxsplit)

    def rstrip(self, chars: str | None = None) -> str:
        """
        Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.as_posix().rstrip(chars)

    def split(self, sep: str | None = None, maxsplit: int = -1) -> list[str]:
        """
        Return a list of the words in the string, using sep as the delimiter string.

        If maxsplit is given, at most maxsplit splits are done (thus, the list will have
        at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is
        no limit on the number of splits (all possible splits are made).

        If sep is given, consecutive delimiters are not grouped together and are
        deemed to delimit empty strings (for example, '1,,2'.split(',') returns
        ['1', '', '2']). The sep argument may consist of multiple characters
        (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']).
        Splitting an empty string with a specified separator returns [''].

        If sep is not specified or is None, a different splitting algorithm is applied:
        runs of consecutive whitespace are regarded as a single separator, and
        the result will contain no empty strings at the start or end if the
        string has leading or trailing whitespace. Consequently, splitting an empty
        string or a string consisting of just whitespace with a None separator
        returns [].
        """
        return self.as_posix().split(sep, maxsplit)

    def splitlines(self, keepends: bool = False) -> list[str]:
        """
        Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        return self.as_posix().splitlines(keepends)

    def startswith(
        self, prefix: str | tuple[str, ...], start: int | None = None, end: int | None = None
    ) -> bool:
        """
        Return True if S starts with the specified prefix, False otherwise.

        prefix can also be a tuple of strings to try. With optional start, test
        S beginning at that position. With optional end, stop comparing S at that
        position.
        """
        return self.as_posix().startswith(prefix, start, end)

    def strip(self, chars: str | None = None) -> str:
        """
        Return a copy of the string with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        return self.as_posix().strip(chars)

    def swapcase(self) -> str:
        """
        Return a copy of the string with uppercase characters converted to lowercase and vice versa.
        """
        return self.as_posix().swapcase()

    def title(self) -> str:
        """
        Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        return self.as_posix().title()

    def translate(self, table: dict[int, int | str | None]) -> str:
        """
        Return a copy of the string in which each character has been mapped through the given translation table.

        The table must implement lookup via __getitem__, e.g. a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None.
        """
        return self.as_posix().translate(table)

    def upper(self) -> str:
        """
        Return a copy of the string converted to uppercase.
        """
        return self.as_posix().upper()

    def zfill(self, width: int) -> str:
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """
        return self.as_posix().zfill(width)
    
class Path(pathlib.Path, StrPath):
    pass

class PosixPath(pathlib.PosixPath, StrPath):
    pass

class PurePath(pathlib.PurePath, StrPath):
    pass

class PurePosixPath(pathlib.PurePosixPath, StrPath):
    pass

class PureWindowsPath(pathlib.PureWindowsPath, StrPath):
    pass

class WindowsPath(pathlib.WindowsPath, StrPath):
    pass