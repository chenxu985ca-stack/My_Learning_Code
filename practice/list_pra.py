# 购物清单
foods = []
prices = []
total = 0

while True:
    food = input("请输入你要买的食物：(按q退出): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"请输入{food}的价格: "))
        foods.append(food)
        prices.append(price)
print("----- 购物清单 -----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"总价为：{total}")
