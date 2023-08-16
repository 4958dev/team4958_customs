from team4958_customs.utils import *

import asyncio
from asyncio import coroutines
import threading

import logging
import traceback

from inspect import isfunction
from typing import Iterable, Any



__all__ = [
    'Asyncio',
    'Threading'
]
log = logging.getLogger(__name__)
DEAFULT_LOOP = asyncio.get_event_loop()



async def _blank():
    pass


    
class Asyncio:
    """
    simplyfies work with `asyncio` which prvides you ability to call coroutines without 'await' expression\n
    -------\n
    loop: asyncio event loop to run your coroutine (highly recommended to specify for every instance uses 'run_threaded' method, but still optional)\n
    to set assign `asyncio.get_event_loop()` to a variable and give it
    """
    def __init__(self, loop:asyncio.AbstractEventLoop=MISSING, **kwargs):
        self.loop = loop
        if 'pass_exceptions' in kwargs.keys():
            if type(kwargs['pass_exceptions']) is bool:
                self.pass_exceptions = kwargs['pass_exceptions']
            else:
                self.pass_exceptions = MISSING
        else:
            self.pass_exceptions = MISSING
        
    def run(self, coro, pass_exceptions: bool=MISSING) -> Any:
        """
        runs your coroutine\n
        can return coroutine result\n
        don't use 'await' expression\n
        -------\n
        pass_exceptions: whether you want to pass all catched exceptions with printing their tracebacks
        """
        if not coroutines.iscoroutine(coro):
            raise TypeError("A coroutine object is required! To run a non-coro function use 'Threading' subclass instead.")
        if pass_exceptions is MISSING:
            if self.pass_exceptions is not MISSING:
                pass_exceptions = self.pass_exceptions
            else:
                pass_exceptions = False
        if pass_exceptions:
            try:
                return asyncio.run(coro)
            except Exception as err:
                log.error(f"passing exception during running coroutine\n{err}", exc_info=True)
                print("passing exception during running coroutine")
                traceback.print_exc()
        else:
            return asyncio.run(coro)
    
    def run_threaded(self, coro, loop:asyncio.AbstractEventLoop=MISSING):
        """
        runs your coroutine without blocking the rest code\n
        this method cannot return anything!\n
        also it always passes exceptions by just printing them\n
        can be used only in async functions\n
        -------\n
        loop: asyncio event loop to run your coroutine (unnecessary if already passed to class instance but may be overriden here)
        """
        if not coroutines.iscoroutine(coro):
            raise TypeError("A coroutine object is required! To run a non-coro function use 'Threading' class instead.")
        async def _exc_pass(obj):
            try:
                await obj
            except Exception as err:
                log.error(f"passing exception during running threaded coroutine\n{err}", exc_info=True)
                print("passing exception during running threaded coroutine")
                traceback.print_exc()
        if loop is MISSING:
            if self.loop is not MISSING:
                loop = self.loop
            else:
                loop = DEAFULT_LOOP
        asyncio.run_coroutine_threadsafe(_exc_pass(coro), loop)

    def kill(self, loop:asyncio.AbstractEventLoop=MISSING):
        """
        safely stops running loop\n
        affects the class instance loop if not specified\n
        if class instance doesn't nave a specified loop too, the deafult event loop will be affected
        """
        if loop is MISSING:
            if self.loop is not MISSING:
                loop = self.loop
            else:
                loop = DEAFULT_LOOP
        if loop.is_running:
            loop.stop()
    
class Threading:
    """
    simplyfies work with `threading` which prvides you ability to use non-coroutines asyncronously\n
    `functions threaded using this class are impossible to stop from code before they finish or stop by themselves!`\n
    also it's impossible to return anything from this
    """
    def __init__(self, **kwargs):
        if 'pass_exceptions' in kwargs.keys():
            if type(kwargs['pass_exceptions']) is bool:
                self.pass_exceptions = kwargs['pass_exceptions']
            else:
                self.pass_exceptions = MISSING
        else:
            self.pass_exceptions = MISSING

    def run(self, func, args: Iterable=MISSING, pass_exceptions: bool=MISSING):
        """
        runs your non-coroutine function threaded\n
        `this method blocks your whole code from being safely stopped/killed until all threads are finished!`\n
        ---------\n
        func: your non-coroutine function (give only a function name here)\n
        args: arguments for function as `(arg1, arg2, ... ,)`\n
        pass_exceptions: whether you want to pass all catched exceptions with printing their tracebacks
        """
        if coroutines.iscoroutine(func):
            raise TypeError("A coroutine object is unacceptable! To run a coroutine function use 'Asyncio' subclass instead.")
        if not isfunction(func):
            raise TypeError("A function is required as 'func' argument!")
        if pass_exceptions is MISSING:
            if self.pass_exceptions is not MISSING:
                pass_exceptions = self.pass_exceptions
            else:
                pass_exceptions = False
        if pass_exceptions:
            try:
                if args is MISSING:
                    args = ()
                thr = threading.Thread(target=func, args=args)
                thr.start()
                thr.join()
            except Exception as err:
                log.error(f"passing exception during running threaded function\n{err}", exc_info=True)
                print("passing exception during running threaded function")
                traceback.print_exc()
        else:
            if args is MISSING:
                args = ()
            thr = threading.Thread(target=func, args=args)
            thr.start()
            thr.join()

    def run_daemon(self, func, args: Iterable=MISSING, pass_exceptions: bool=MISSING):
        """
        runs your non-coroutine function daemon-threaded\n
        `safe for stopping/killing your program anytime but never run critical tasks with this`\n
        ---------\n
        func: your non-coroutine function (give only a function name here)\n
        args: arguments for function\n
        pass_exceptions: whether you want to pass all catched exceptions with printing their tracebacks
        """
        if coroutines.iscoroutine(func):
            raise TypeError("A coroutine object is unacceptable! To run a coroutine function use 'Asyncio' subclass instead.")
        if not isfunction(func):
            raise TypeError("A function is required as 'func' argument!")
        if pass_exceptions is MISSING:
            if self.pass_exceptions is not MISSING:
                pass_exceptions = self.pass_exceptions
            else:
                pass_exceptions = False
        if pass_exceptions:
            try:
                if args is MISSING:
                    args = ()
                thr = threading.Thread(target=func, args=args, daemon=True)
                thr.start()
                thr.join()
            except Exception as err:
                log.error(f"passing exception during running threaded function\n{err}", exc_info=True)
                print("passing exception during running threaded function")
                traceback.print_exc()
        else:
            if args is MISSING:
                args = ()
            thr = threading.Thread(target=func, args=args, daemon=True)
            thr.start()
            thr.join()