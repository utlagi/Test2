## How about having a "def" file that defines the abstract classes of concern
## https://www.python.org/dev/peps/pep-0484/

from threading import Thread, ThreadError
import inspect


__test_interfaces = False
NoneType = type(None)

verbose = True
vverbose = False


def verbose_print(*s):
    if verbose:
        print(" ".join(map(str, s)))


def vverbose_print(*s):
    if vverbose:
        print(" ".join(map(str, s)))


def method_name():
    return inspect.currentframe().f_back.f_code.co_name



