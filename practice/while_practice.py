num = int(input("input a # (1 - 10)): "))

while num < 1 or num > 10:
    print('Invalid input, please try again.')
    num = int(input("input a # (1 - 10)): "))
print(f'You input number is {num}.')
