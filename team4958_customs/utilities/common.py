"""
some useful common classes and functions
"""
import pathlib

from team4958_customs.utils import ROOT



def MkPath(path:str):
    """
    creates a `Path` object from string\n
    use single slashes, backslashes or commas as splitters but don't mix them\n
    the starting point of this path will be your project root directory anyway
    """
    res = ROOT
    if type(path)==str:
        if '/' in path:
            path_elements = path.split('/')
            for el in path_elements:
                res = pathlib.Path(res, el)
            return res
        if '\\' in path:
            path_elements = path.split('\\')
            for el in path_elements:
                res = pathlib.Path(res, el)
            return res
        if ', ' in path:
            path_elements = path.split(', ')
            for el in path_elements:
                res = pathlib.Path(res, el)
            return res
        if ',' in path:
            path_elements = path.split(',')
            for el in path_elements:
                res = pathlib.Path(res, el)
            return res