import shutil

try:
    shutil.copyfile('text.tx', 'copy.txt')
except:
    print("FileNotFoundError")
