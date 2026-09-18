# 创建并写入一个文件

file_text = "兄弟啊，我想你啦!"

file_path = "text.txt"
# with open(file_path, 'a') as file:    #append
# with open(file_path, 'x') as file:    #
with open(file_path, 'w') as file:  # write
    file.write(file_text)
    print("This file has created")
