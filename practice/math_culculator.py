# 数学计算器
operater = input("please input operater(+,-,*,/) : ")
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))

if operater == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operater == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operater == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operater == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print(f"{operater} it's not a operater")
