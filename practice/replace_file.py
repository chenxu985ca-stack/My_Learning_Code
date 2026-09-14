import os

sourse = "coy.txt"

destination = "/Users/lee/Desktop/copy.txt"

try:
    if os.path.exists(destination):
        print("这里已经有一个同样的文件了")
    else:
        os.replace(sourse, destination)
        print("该文件已经成功移动")
except FileNotFoundError:
    print(sourse + "没找到")
