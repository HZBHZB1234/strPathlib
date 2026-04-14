from pathlib import Path
from typing import Callable

class Path(Path):
    def __getattribute__(self, __name: str):
        if not hasattr(self, __name):
            func: Callable = getattr(str, __name)
            return lambda *args, **kwargs : func(self.__str__(*args, **kwargs))
        else:
            return getattr(__name)