import os

print(os.getcwd())
print(os.path.abspath(os.path.relpath(__file__)))
# print(os.path.relpath('/home/andrey/repo/python/python_task/', start=None))
# print('breakpoint')
print(os.path.relpath('//', start=None))
print(os.path.relpath(__file__))
