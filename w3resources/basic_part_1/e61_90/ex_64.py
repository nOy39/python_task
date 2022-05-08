"""64. Write a Python program to get file creation and modification date/times."""

import os, time


file_name = 'ex_list'
ctime = time.ctime(os.path.getctime(file_name))
mtime = time.ctime(os.path.getmtime(file_name))
test = os.path.isfile(file_name)
print('===' * 5)
print('File name: ', file_name)
print('===' * 5)
print(f'Created: {ctime}')
print(f'Modified: {mtime}')
