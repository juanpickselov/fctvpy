import sys

from item_01 import show_me_sys_info


def show_the_version():
    show_me_sys_info()


def show_the_copyright():
    print(sys.copyright)
