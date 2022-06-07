"""
调用 gifsicle 压缩gif
"""
import sys
import os

if len(sys.argv) == 1:
    print('gif.py <file>')
    exit()

file = sys.argv[1]
cli = ".\gifsicle-x64\gifsicle.exe --no-warnings --no-app-extensions --optimize=3 --colors=256 {} -o {}".format(file, file)
print(os.system(cli))