"""
调用 cjpeg 压缩jpg
"""
import sys
import os

quality = 75  # 图片品质 (0..100; 5-95 is most useful range, default is 75)

if len(sys.argv) == 1:
    print('jpg.py <file> [quality=75]')
    exit()
elif len(sys.argv) == 3:
    quality = sys.argv[2]

file = sys.argv[1]
tmpfile = file + '.tmp'
cli = ".\mozjpeg-x64\cjpeg-static.exe -quality {} {} > {}".format(quality, file, tmpfile)
print(os.system(cli))
try:
    print(os.remove(file))
except Exception as e:
    print(e)
    print(os.remove(tmpfile))
try:
    print(os.rename(tmpfile, file))
except Exception as e:
    print(e)
