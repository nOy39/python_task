"""TODO test by linux and windows"""
"""Write a python program to call an external command in Python"""

import platform, os, subprocess

type_os = platform.platform()[:3].lower()
print(platform.platform())

if type_os != 'win':
    subprocess.call(["ping", "c -2", "www.ya.ru"])
else:
    os.system('calc')
