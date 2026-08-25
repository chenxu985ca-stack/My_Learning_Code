print('My favorite colors are', 'blue', 'green', 'red')

print('你好', '世界!')
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(msg, quote)


my_none_var = None
print('None:', my_none_var)  # None: None

developer = "lee"
print(type(developer))  # <class 'str'>
print(type(1))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type(True))  # <class 'bool'>

account_balance = "15"
print(isinstance(account_balance, int))

account_balance = 55
print(isinstance(account_balance, (int, float)))

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age)  # John Doe26

my_str = 'Hello world'
print(my_str[::-1])  # dlrow olleH

love_str = 'I love Python!'
split_words = love_str.split()
print(split_words)


user_id = "chenxu-985-ca"
print(user_id[-4:])

print("Hello, World")

print("Hello, World")


my_int_1 = 2
my_int_2 = 3

my_float_1 = 2.0
my_float_2 = 3.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_2 ** my_float_1
print(exp_ints)
print(exp_floats)

my_int_1 = 2
my_int_2 = 3

my_float_1 = 2.0
my_float_2 = 3.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints)  # Integer Exponentiation: 8
print('Float Exponentiation:',  exp_floats)  # Float Exponentiation: 9.0
