"""Write a python program to access environment variables."""

import os


def print_path(_str_path):
    path_list = _str_path.split(':')
    for i in path_list:
        print(i)
    pass


env_vars = os.environ
for var in env_vars:
    print('---' * 30)
    if env_vars[var].find(':') > 0:
        print(f'{var}: \n')
        print_path(str(env_vars[var]))
    else:
        print(f'{var} : {env_vars[var]}')

