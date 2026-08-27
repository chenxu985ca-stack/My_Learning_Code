# temp 转换器
unit = input("Type unit(C/F): ")
temp = float(input("Type tempreture: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"转换为华氏度为：{temp}℉")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"转换为摄氏度为：{temp}℃")
else:
    print(f"{unit} is not a real unit")
