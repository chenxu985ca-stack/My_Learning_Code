menu = {
    "hamberger": 17.0,
    "cole": 8.0,
    "potatos": 9.9,
    "chickens": 13.5,
    "lemonade": 7.0}

for name, price in menu.items():
    menu[name] = round(price * 0.8)

print(f"{menu}")
