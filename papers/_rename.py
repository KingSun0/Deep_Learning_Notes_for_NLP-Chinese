"""
重命名在文件夹内的所有文件名，将文件名中的所有空格替换为指定字符

使用方法，在当前文件夹下运行 "python tool-rename.py"
"""
import os
# import huaytools

NEW_CHAR = '-'

dirpath = "."

for dirpath, dirnames, filenames in os.walk(dirpath):
    print(filenames)
    for fn in filenames:
        new_fn = fn.replace(' ', NEW_CHAR)
        if new_fn != fn:
            os.rename(os.path.join(dirpath, fn), os.path.join(dirpath, new_fn))



