# 复利计算器

Principal = 0
Interest = 0
Times = 0

while True:
    Principal = float(input("请输入本金(大于0):"))
    if Principal < 0:
        print("本金必须大于等于0请重新输入。")
    else:
        break

while True:
    Interest = float(input("请输入利息(大于等于0):"))
    if Interest < 0:
        print("利息必须大于0请重新输入。")
    else:
        break

while True:
    Times = int(input("请输入年份(大于等于0):"))
    if Times < 0:
        print("年份必须大于0请重新输入。")
    else:
        break

total = Principal * pow((1 + Interest / 100), Times)

print(f"本金:{Principal}元, 利息:{Interest}%, 年数:{Times}年")
print(f"最终金额:¥{total:.2f}")
