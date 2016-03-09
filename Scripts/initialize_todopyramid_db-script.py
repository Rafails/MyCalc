#!C:\Users\rafal\Desktop\mycalc\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'todopyramid','console_scripts','initialize_todopyramid_db'
__requires__ = 'todopyramid'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('todopyramid', 'console_scripts', 'initialize_todopyramid_db')()
    )
