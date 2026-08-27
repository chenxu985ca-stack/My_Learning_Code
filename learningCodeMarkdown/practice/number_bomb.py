# 数字炸弹小游戏啊

num = 15

length = int(input("输入你唧唧的长度： "))

while length > 0:
    if length > num:
        print("哥哥唧唧好大，但是太大了顶的不舒服")
        length = int(input("罚你重新输一遍： "))

    elif length == 15:
        print("哥哥长度刚好顶到我的花心了，好喜欢")
        break
    else:
        print("哥哥唧唧太小了，没感觉")
        length = int(input("罚你重新输一遍： "))

else:
    print("总不能是凹进去的吧： ")
    length = int(input("罚你最后重新输一遍： "))

print(f"对了，唧唧和花心的长度一样")
