#!C:\Users\rafal\Desktop\mycalc\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'MyProject','console_scripts','initialize_MyProject_db'
__requires__ = 'MyProject'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('MyProject', 'console_scripts', 'initialize_MyProject_db')()
    )
