"""TODO test by linux and windows"""
"""Write a Python program to get OS name, platform and release information."""

# Use module platform.

from platform import uname

os_data = uname()
print('OS name: %s, platform: %s, release: %s' % (os_data[0], os_data[2], os_data[3]))
