import os
import shutil

path = "folder"
try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path)  # 慎用，这行代码会删除掉文件及里面所有的内容
except FileNotFoundError:
    print(f"This {path} not found!")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("This folder was not empty")
else:
    print(path + " was deleted")
