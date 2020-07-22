#!C:\Users\heman\PycharmProjects\Python\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'memory-usage-notifier==1.1','console_scripts','checkMem'
__requires__ = 'memory-usage-notifier==1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('memory-usage-notifier==1.1', 'console_scripts', 'checkMem')()
    )
