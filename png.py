"""
调用 pngquant 压缩png
"""
import sys
import os

if len(sys.argv) == 1:
    print('png.py <file>')
    exit()

file = sys.argv[1]
path = os.path.split(os.path.realpath(__file__))[0]
cli = path + ".\pngquant\pngquant.exe {} --force --output {}".format(file, file)
print(os.system(cli))