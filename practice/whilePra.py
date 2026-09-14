# while

prompt = "\n如果你可以随心选择居住地，你最想住哪里？（q to end this program）:"


while True:
    message = input(prompt)

    if message == 'q'.lower():
        break
    else:
        print(f"{message} 是个好地方")

# ---------------------------------------

unconfirmed_users = ['alice', 'jack', 'brain']

confirmed_users = []

while unconfirmed_users:
    curren_user = unconfirmed_users.pop()
    print(f"{curren_user} ,未注册")
    confirmed_users.append(curren_user)

print("\nafter a while-----\n")
print(f'{confirmed_users} has already done')
