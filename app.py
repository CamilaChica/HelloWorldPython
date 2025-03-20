# Working with Directories
from pathlib import Path

# Absolute path - to refer a Directory in a computer
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative path - to refer a File inside our current Directory
# path = Path("ecommerce")
# print(path.exists()) #We check if the path exists
# path = Path("emails")
# print(path.mkdir()) #We create a new Directory
# print(path.rmdir()) #We delete a new Directory

# path = Path()
# print(path.glob('*')) # We can look at all the Directories in this project
# print(path.glob('*.*')) # We can look at all the Files in this project

# Search for Files only:
path = Path()
for file in path.glob('*.py'):
    print(file)

# Search for Files and Directories:
path = Path()
for file in path.glob('*'):
    print(file)