"""
if you are tired of recreating same project structures again and again
--------
"""



from team4958_customs.utilities.assets import builder_presets
from team4958_customs.utils import ROOT, MISSING, MAXINT, _yesornot

import pathlib
from pathlib import Path

import os


__all__ = [
    'Build'
]



NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
LOWERCASES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALLOWED_SYM = ['_']
UNRECOMMENDED_SYM = [' ','(',')','-',"'",';']

RESTRICTED = ['`', '~', '!', '@', '#', '$','^','&','*','=','+','?','{','}',':','<',',','.','>','№','|','/','\\','"']
ALLOWED = NUMBERS+LOWERCASES+ALLOWED_SYM
UNRECOMMENDED = UPPERCASES+UNRECOMMENDED_SYM



class _Check:
    def sym_presence(string:str, sym_list:list):
        """
        checks if symbols from listing are present in string
        """
        res = []
        string = list(set(list(string)))
        for sym in string:
            if sym in sym_list:
                res.append(sym)
        if res!=[]:
            return res
        else:
            return



def _projectname():
    from sys import setrecursionlimit as recurlim
    recurlim(MAXINT)
    name = input("give your project a proper name: ")
    restricted = _Check.sym_presence(name, RESTRICTED)
    unrecommended = _Check.sym_presence(name, UNRECOMMENDED)
    if name=='':
        print('name cannot be empty!')
        return _projectname()
    elif restricted:
        print(f"there are some restricted symbols in project name given: {restricted}")
        return _projectname()
    elif unrecommended:
        confirm = _yesornot(f'there are some unrecommended symbols in project name!\nsymbols checker didnt like: {unrecommended}\ndo you really wish to keep it like that?')
        if confirm:
            return name
        else:
            return _projectname()
    else:
        return name



def _fromdict(obj:dict, path=MISSING):
        """
        `NEVER FUCKING CALL THIS INSIDE YOUR CODE`
        ------------
        \n
        this will spawn your whole structure directly in current work directory!\n
        `use 'fromdict' method instead`\n
        --------\n
        builds a project structure from dict
        ----
        \n
        -------\n
        example_dict = {
            'folder_name':{
                #feel free to make as much substructures as you need
            },
            'filename.extension':['line1', 'line2', 'line3', etc.],
            'filename2.extension':'any text to put inside the file just as string'
        }
        """
        if path is MISSING:
            path = ROOT
        for (key, val) in obj.items():
            if type(val) is dict:
                try:
                    os.mkdir(pathlib.Path(path, key))
                except FileExistsError:
                    pass
                newpath = pathlib.Path(path, key)
                _fromdict(val, newpath)
            elif type(val) is list or type(val) is str:
                with open(pathlib.Path(path, key), 'w') as f:
                    if type(val) is list:
                        if val!=[]:
                            for line in val:
                                f.write(f'{line}\n')
                    else:
                        f.write(val)
            else:
                print(f'"{key}" type not specified as file or folder, skipping...')



class Build:
    """builds a project template from preset inside a subfolder named as your project"""

    def blank(name: str=MISSING, create_subfolder=True, readme=True, requirements=True, license_file=False):
        """
        blank preset which creates `src` folder and `main.py` file without anything inside
        ---------
        \n
        also creates empty `README.md`, `requirements.txt` and `LICENSE` files\n
        ---------\n
        name: name of your project folder (if not specified inside the code will be asked through console)\n
        required when create_subfolder is 'True' (which is deafult)\n
        --------------\n
        create_subfolder: whether you wish to create a subfolder for your project (builds template in a current directory if 'False')\n
        -------\n
        readme: whether you wish to create a `README.md` file in your project's root directory\n
        -------\n
        requirements: whether you wish to create a `requirements.txt` file in your project's root directory\n
        ---------\n
        license_file: whether you wish to create a `LICENSE` file in your project's root directory (will be empty)
        """
        if create_subfolder == False:
            proj_path = ROOT
        else:
            if name is MISSING:
                name = _projectname()
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
            else:
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
        with open(Path(proj_path, 'main.py'), 'w') as f:
            pass
        if readme:
            with open(Path(proj_path, 'README.md'), 'w') as f:
                pass
        if requirements:
            with open(Path(proj_path, 'requirements.txt'), 'w') as f:
                f.write("team4958_customs")
        if license_file:
            with open(Path(proj_path, 'LICENSE'), 'w') as f:
                pass
    
    def fromdict(preset:dict, name: str=MISSING, create_subfolder=True):
        """
        builds a project structure from dict
        ----
        \n
        ---------\n
        preset: your own structure preset presented as dictionary
        \n
        example_dict = {\n
            'folder_name':{\n
                #feel free to make as much substructures as you need\n
            },\n
            'filename.extension':['line1', 'line2', 'line3', etc.],\n
            'filename2.extension':'any text to put inside the file just as string'\n
        }\n
        -------\n
        name: your project's name (required and has its point only if 'create_subfolder' is True)\n
        create_subfolder: whether you wish to create everything inside a subfolder\n
        """
        if create_subfolder == False:
            proj_path = ROOT
        else:
            if name is MISSING:
                name = _projectname()
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
            else:
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
        _fromdict(preset, path=proj_path)
    
    def deafult(name: str=MISSING, create_subfolder=True):
        """
        builds a project structure from built-in deafult template
        ----
        \n
        ---------\n
        name: your project's name (required and has its point only if 'create_subfolder' is True)\n
        create_subfolder: whether you wish to create everything inside a subfolder\n
        """
        if create_subfolder == False:
            proj_path = ROOT
        else:
            if name is MISSING:
                name = _projectname()
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
            else:
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
        _fromdict(builder_presets.DEAFULT, path=proj_path)
        
    def disnake_bot(name: str=MISSING, create_subfolder=True):
        """
        builds a disnake bot project structure from built-in template
        ----
        \n
        ---------\n
        name: your project's name (required and has its point only if 'create_subfolder' is True)\n
        create_subfolder: whether you wish to create everything inside a subfolder\n
        """
        if create_subfolder == False:
            proj_path = ROOT
        else:
            if name is MISSING:
                name = _projectname()
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
            else:
                try:
                    os.mkdir(Path(ROOT, name))
                except FileExistsError:
                    pass
                proj_path = Path(ROOT, name)
        _fromdict(builder_presets.DISNAKE, path=proj_path)



class Package:
    def __init__(self):
        pass

    def _pack():
        pass
    
    def _unpack():
        pass