"""
if you are tired of recreating same project structures again and again
--------
"""



from team4958_customs.utilities.assets.builder_presets import *
from team4958_customs.utils import ROOT, MISSING, _yesornot
from team4958_customs.abc import NUMBERS, LOWERCASES, UPPERCASES, ALLOWED_SYM, UNRECOMMENDED_SYM, RESTRICTED_SYM as RESTRICTED

from pathlib import Path

import os


__all__ = [
    'Build'
]



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

        if name is MISSING and create_subfolder==True:
            name = _projectname()
        os.mkdir(Path(ROOT, name, 'src'))
        with open(Path(ROOT, name, 'main.py'), 'w') as f:
            pass
        if readme:
            with open(Path(ROOT, name, 'README.md'), 'w') as f:
                pass
        if requirements:
            with open(Path(ROOT, name, 'requirements.txt'), 'w') as f:
                f.write("team4958_customs")
        if license_file:
            with open(Path(ROOT, name, 'LICENSE'), 'w') as f:
                pass