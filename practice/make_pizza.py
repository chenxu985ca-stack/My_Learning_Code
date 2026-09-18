def make_pizza(size, *toppings):
    print(f"A {size}cm pizza whith", end=" ")

    for topping in toppings:
        print(topping, end=" ")
