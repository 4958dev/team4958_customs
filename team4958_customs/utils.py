from typing import Any

import pathlib



__all__ = [
    'MISSING',
    'ROOT',
    'MAXINT'
]



ROOT = pathlib.Path(pathlib.Path.cwd())
MAXINT = 2147483647



class _MissingSentinel():
    def __eq__(self, other: Any) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "..."

MISSING: Any = _MissingSentinel()



def _yesornot(text):
    from sys import setrecursionlimit as recurlim
    recurlim(MAXINT)
    """
    repeats question until user answers `yes` or `no`
    """
    print(text, ' (y/n) ', end='')
    answer = input()
    if answer=='y' or answer=='Y' or answer=='yes' or answer=='Yes' or answer=='YES':
        return True
    elif answer=='n' or answer=='N' or answer=='no' or answer=='No' or answer=='NO':
        return False
    else:
        return _yesornot(text)