"""Write a python program to call an external command in Python"""

import os
import platform

type_os = platform.platform()[:3].lower()
print(platform.platform())

if type_os != 'win':
    os.system('ls -l')
else:
    os.system('calc')
