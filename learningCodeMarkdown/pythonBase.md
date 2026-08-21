## Python学习的Markdown
### 什么是Python？
Python 是一种通用编程语言，以其简洁和易用性而著称。
#### 用途
- Python 被广泛数据科学和机器学习、网页开发、脚本与自动化、嵌入式系统、物联网等多个领域。
- 网络安全专业人士和道德黑客使用 Python 来检测恶意软件和其他病毒等漏洞，构建自动化安全扫描工具，并分析威胁。
- Python 在树莓派等微型计算机以及兼容 MicroPython 的开发板上运行良好，因此你可以构建各种物联网项目，例如智能家居设备、气象监测站等。
- Python 在 DevOps 中被广泛用于编写 CI/CD 脚本以及管理开发流水线中的基础设施。它也常用于构建后端服务和内部 API。
#### 扩展
Pandas 和 NumPy 等数据库使数据分析变得不那么繁琐，
TensorFlow 和 Scikit-learn 等工具则让机器学习以及与人工智能模型的协作变得更加容易上手。
#### 框架
在网页开发中，*Django*、*FastAPI* 和 *Flask* 等 Python 框架使开发者能够以==最小==的努力构建可扩展且安全的后端系统。
#### 优势
Python 最大的优势之一就是自动化。你可以编写简单的脚本，来帮助你完成诸如从电子表格中提取数据、发送电子邮件以及在本地机器上处理文件等重复性任务。

Python 是任何想学习编程的人的绝佳选择，无论他们将来选择专攻哪个领域。

---
### 变量和数据类型
在 Python 中声明变量时，使用赋值操作符（=）将一个值分配给标识符。

#### 声明变量
```ruby
name = "lee"
age = 24
```
- 变量名只能以字母或下划线（_）开头，不能以数字开头。

- 变量名只能包含字母数字字符（a-z、A-Z、0-9）和下划线（_）。

- 变量名区分大小写：`age`、`Age` 和 `AGE` 被视为不同的名称。

- 变量名不能是 Python 的保留关键字，例如 `if`、`class` 或 `def`。
  
如果你违反了其中任何一条规则，你的 Python 程序将会抛出一个 SyntaxError：

```ruby
5variable_name = 5
 ^
SyntaxError: invalid syntax
```
#### 常用的命名规范
1. 变量名应使用小写字母，并用下划线分隔单词。这被称为蛇形命名法：
```ruby
my_wechat_name = '李宸旭'
```

2. 变量名应该使用描述性名称，例如：
```ruby
my_age = 24
```
使用 `my_age` 比 `age` 或 `ua` 这样的缩写更合适。

3. 避免使用单字母变量名,因为它们无法传达任何用途或含义,例如：
```ruby
x = 1
#x是什么东西？什么意思？
```
4. 使用注释#解释代码、给自己留提醒，或说明某一行代码存在的原因。在学习或团队协作时，注释尤其有帮助。
```ruby
#这就是我学习的笔记
```

---

### `print()`函数的用法
学习任何编程语言时，你做的第一件事之一就是编写一个简单的“Hello world!”程序。
#### 打印一个参数
```ruby
print('Hello world!') # Hello world!
```
#### 打印多个参数
使用 `print()` 函数一次性显示多个值或参数，只需用逗号分隔即可。
```ruby
print('My favorite colors are', 'blue', 'green', 'red')
# 输出: My favorite colors are blue green red
```
Python 会自动在用==逗号==分隔的每个项目之间添加==空格==。当你希望将多个信息一起打印时，这非常有用。

---


### Python与其他语言的对比
Python 是一种==动态类型语言==，类似于 JavaScript，
#### Python声明变量
意味着你无需显式声明变量的类型。语言会根据你为变量赋值的内容来判断其数据类型。
```ruby
name = 'John Doe' # Python会识别这是一个字符串
age = 25 # Python会识别这是一个数字
```
#### 其他语言声明变量
C#、Java和C++等静态类型语言不同，在这些语言中，必须像这样为变量声明类型：
```ruby
string name = "John Doe";
int age = 25;
```
#### Python的特性优缺点

Python 的动态类型特性使编码更快速、更灵活，但也可能导致意外的错误
>[!WARNING]
因为类型错误只有在程序运行时才会被检测到，而不是在编译时。由于 Python 在程序运行时确定数据类型，因此与类型相关的错误只能在运行时才被发现。

相比之下，有些语言会在程序运行前进行编译。编译意味着计算机会预先检查你的代码，并将其准备就绪以便运行。在此过程中，这些语言甚至可以在程序开始之前就捕获类型错误。

---

### Python的常用数据类型
- `Integer`: 没有小数点的整数, 例如：`10` 或者 `-5`。
```ruby
my_integer_var = 10
print("Integer: ",my_integer_var)#输出Integer: 10
```
- `Float`: 带小数点的数字，例如`4.21`或者`-3.14`。
```ruby
my_Float_var = 3.141
print("Float: ",my_Float_var)#输出Float: 3.141
```
- `String`: 由**单引号或双引号**括起的一串字符，例如 `'Hello world!'`。
```ruby
    my_string_var = 'hello'
    print('String: ', my_string_var) # String: hello
```
- `Set`: 由**花括号**包围的一个==无序的唯一元素==集合，例如 `{0.5, 4, 'apple'}`。
```ruby
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {8.5, 'hello', 7} (顺序各不相同)
```
- `Dictionary`: 由**花括号**包围的一组==键值对==，例如 {'name': 'John Doe', 'age': 28}。
```ruby
my_dictionary_var = {'name': 'lee', 'age': 24}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'lee', 'age': 24}
```
- `Tuple`: 一种不可变的==有序集合==，用**括号**括起，例如 ('apple', 4.5, 7)。
```ruby
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
```
- `Range`: 一组数字，常用于循环中，例如 range(5)。
```ruby
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
```
- `List`:用[ ]包围的，一种==有序==的元素集合，支持多种数据类型。
```ruby
 my_list_var = [22, 'Hello world', 3.14, True]
print('List:', my_list_var) # List: [22, 'Hello world', 3.14, True]
```
- `None`：表示值不存在的特殊值。
```ruby
my_none_var = None
print('None:', my_none_var) # None: None
```
---

### 查看变量的类型
#### `type()` 函数
想要查看变量的类型，可以使用`type()`函数：
```ruby
developer = “lee”
print(type(developer))# <class 'str'>
```
`type()`函数的参数不能为空
```ruby
type()
#会报下面这个错误
#TypeError: type() takes 1 or 3 arguments
```
下面是我们所学到的所有数据类型，type( )函数对他们的输出结果：
```ruby
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
```

#### `isinstance()`函数
在程序中，有时需要在对某个变量执行操作之前，先验证其是否具有特定类型。
```ruby
account_balance = "15"
isinstance(account_balance, int)#这行代码是在确定account_balance是不是整数
```
`isinstance()`函数还可以让你一次性检查多种类型，例如：
```ruby
account_balance = 55.08
isinstance(account_balance,(int,float))
```

---

### 什么是字符串，以及字符串的不可变性是什么？
字符串是由``' '``或`" "`包围的一系列字符。
#### 字符串的符号表达
```ruby
my_str_one = "one"
my_str_two = 'two'
```
如果需要多行字符串，可以使用`""" """`或`''' '''`：
```ruby
my_str_three = """
多行
字符串
"""
my_str_four =‘’‘
多行
字符
串
’‘’
```
如果你的字符串中含有`""` 或者 `''`，那么你可以通过两种方式来表达：
1. 用相反类型的引号，例如：
```ruby
msg = "It's a nice day!"
quote = 'She said"Hello! My name is sally."'
```
1. 使用`\`来转义字符串中的单引号或双引号。通过这种方法，你可以使用单引号或双引号来包裹字符串本身：
```ruby
msg = 'It\'s a nice day!'
quote = "She said \"Hello My name is sally.\""
```
#### `in` 运算符
有时，你可能需要检查一个字符串是否包含一个或多个字符。为此，Python 提供了 `in` 运算符，它返回一个布尔值，用于判断该字符或字符是否存在于字符串中：
```ruby
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```
#### `len()` 函数
要获取字符串的长度，可以使用内置的 `len()` 函数，例如：
```ruby
my_str = 'Hello world'
print(len(my_str))  # 11
```
#### 字符串索引
字符串中的每个字符都有一个称为索引的位置。索引从零开始，即字符串第一个字符的索引是0，第二个字符的索引是1，依此类推。要通过索引访问某个字符，需使用方括号`[]`并将要访问的字符的索引放在方括号内，例如：
```ruby
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```
负数索引也是允许的，因此你可以通过 -1 获取任意字符串的最后一个字符，-2 获取倒数第二个字符，以此类推：
```ruby
my_str = "Hello world"

print(my_str[-1])  # d
print(my_str[-2])  # l
```
#### 字符串的不可变性
Python 并没有严格区分‘原生类型’ 和 ‘引用类型’，所有数据都被视为对象，其中一些对象是不可变的，而另一些则是可变的。
不可变数据类型一旦声明后就无法修改或更改。你可以将变量指向新的对象，这称为重新赋值，但不能通过添加、删除或替换其任何元素来改变原始对象本身。
而字符串就是 Python 中**不可变**的数据类型。这意味着你可以将不同的字符串重新赋值给一个变量：
```ruby
greeting = 'hi'
greeting = 'hello'
print(greeting) # 输出hello
```
但不允许直接修改字符串：
```ruby
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

---

### 什么是字符串拼接和字符串插值？
在处理字符串时，将不同的文本片段组合在一起是一种常见的操作，你经常会遇到这种情况。
#### 连接字符串
在 Python 中，你可以使用加号`+`运算符将多个字符串连接在一起。这个过程称为字符串拼接。以下是使用加号运算符连接两个字符串的方法：
```ruby
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) #输出Hello World
```
#### 重复字符串
你也可以使用 * 运算符将字符串乘以一个整数来重复字符串，字符串将被指定次数重复：
```ruby
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # 输出hahaha
```
#### ~~将字符串与数字连接~~
连接操作仅适用于字符串。如果尝试将字符串与数字连接，将会得到 TypeError 错误：
```ruby
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```
这是因为当你连接其他数据类型（如整数）时，Python 会自动将它们转换为字符串。Python 要求所有元素都必须是字符串才能进行连接操作。要解决这个问题，你可以使用内置的 `str()` 函数将数字转换为字符串，`str()`函数会返回给定对象的字符串表示形式，而不会修改原始对象：
```ruby
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```
也可以使用**增强赋值运算符**进行字符串拼接。该运算符由加号和等号`+=`表示，可以在一步中同时完成拼接和赋值操作。例如：
```ruby
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```
#### 字符串插值
将变量和表达式插入字符串的过程称为字符串插值。Python 中有一类字符串叫做`f`字符串（即格式化字符串字面量），它允许你使用简洁且易读的语法来处理插值操作。
`F`字符串以 `f`（小写或大写）开头，位于引号之前，允许你在花括号(`{}`)指示的替换字段中嵌入变量或表达式。例如：
```ruby
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) 
# My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') 
# The sum of 5 and 10 is 15
# 数字 5 加 10 等于 15
```
请注意，您无需使用 str() 函数将非字符串类型进行转换。在上面的例子中，`age`、`num1` 和 `num2` 变量的值在插值过程中会自动被转换为字符串。
#### 什么是字符串切片及如何切片？
字符串切片允许你提取字符串的一部分，或仅处理其特定区域。以下是基本语法：
```ruby
string[start:stop]
```
如果你想从某个索引提取到另一个索引的字符，只需用冒号分隔起始和结束索引即可：
```ruby
my_str = 'Hello world'
print(my_str[0:4]) # Hell
```
==注意==，停止索引是**不包含**的，因此 `[0:4]` 只提取了从索引 `0` 开始，到索引 `4`（但不包括索引 `4`）为止的字符。

你也可以省略起始和结束索引，Python 将分别默认为`0`或字符串的末尾。例如，如果省略起始索引，会发生如下情况：
```ruby
my_str = 'Hello world'
print(my_str[:7])  # Hello w
```
这会提取从索引`0`开始，直到（但不包括）索引7处的字符。如果省略停止索引，则会发生以下情况：
```ruby
my_str = 'Hello world'
print(my_str[8:])  # rld
```
从索引8处的字符开始，提取到字符串末尾的所有内容。
==注意==，切片字符串不会修改原始字符串：
```ruby
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world
```
你也可以省略起始和结束索引，这样就会提取整个字符串：
```ruby
my_str = 'Hello world'
print(my_str[:])  # Hello world
```
除了起始和结束索引外，还有一个可选的步长参数，用于指定切片中每个索引之间的增量。

Here's the syntax for that:
这是该语法的写法：
```ruby
string[start:stop:step]
```
在下面的例子中，切片从索引 `0` 开始，停止在 `11` 之前，并提取每隔一个字符：
```ruby
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```
使用 `step` 参数的一个实用技巧是，将 `step` 设置为 `-1`，同时不指定 `start` 和 `stop`，即可反转字符串：
```ruby
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

---

### 有哪些常见的字符串方法？
Python 提供了多种内置方法，可用于操作字符串，包括但不限于以下内容：
- `upper()`：返回一个所有字符转换为大写的字符串。
```ruby
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```
- `lower()`：返回一个所有字符转换为小写的字符串。
```ruby
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```
- `strip()`：返回一个移除指定前后字符的新字符串。如果未传入参数，则移除首尾的空白字符。
```ruby
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```
- `replace(old, new)`：返回一个新字符串，其中所有旧字符串被新字符串替换。
```ruby
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```
- `split(separator)`：根据指定的分隔符将字符串拆分为字符串列表。如果未指定分隔符，则按空格进行拆分。
```ruby
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```
- `join(iterable)`：将可迭代对象的元素用分隔符连接成一个字符串。
```ruby
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```
- `startswith(prefix)`：返回一个布尔值，表示字符串是否以指定前缀开头。
```ruby
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```
- `endswith(suffix)`：返回一个布尔值，表示字符串是否以指定的后缀结尾。
```ruby
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```
- `find(substring)`：返回子字符串**首次**出现的位置，如果未找到则返回 -1。
```ruby
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```
- `count(substring)`：返回子字符串在字符串中出现的次数。
```ruby
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```
- `capitalize()`：返回一个新字符串，首字母大写，其余字符小写。
```ruby
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```
- `isupper()`：如果字符串中的所有字母都是大写，则返回 True，否则返回 False。
```ruby
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```
- `islower()`：如果字符串中的所有字母都是小写，则返回 True，否则返回 False。
```ruby
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```
- `title()`: 返回一个新字符串，其中每个单词的首字母大写。
```ruby
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

---

### 数学与数学运算
#### 整数和浮点数
整数和浮点数都可以是正数或者负数
都可以进行`+` `-` `*` `/`运算
数 
```ruby
my_int_1 = 50
my_int_2 = 2
#加
sum_ints = my_int_1 + my_int_2
#减
diff_ints = my_int_1 - my_int_2
#乘
product_ints = my_int_1 * my_int_2
#除
div_ints = my_int_1 / my_int_2
```
```ruby
my_float_1 = 50
my_float_2 = 2
#加
sum_ints = my_float_1 + my_float_2
#减
diff_ints = my_float_1 - my_float_2
#乘
product_ints = my_float_1 * my_float_2
#除
div_ints = my_float_1 / my_float_2
```
如果将整数和浮点数混合`+` `-` `*` `/`,结果会自动转换为浮点
```ruby
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>
```
#### 取模运算%
```ruby
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1
#求整数商：q =  a / b  （a 除以 b，结果向下取整）
#计算余数：r = a - b * q

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993
#例如：被除数=7  除数=3
#1. 被除数大于除数，余数为 = 7 - 3 * 2 = 1
#2. 被除数小于除数，余数为除数本身r = 3 - 7 * 0 = 3
#3. 负数取模，不同的语言会不一样
#Python：-7 - 3 * (-3) = 2 （数学上的取模 Modulo）
#C / C++ / Java / JS：-7 - 3 * (-2) = -1（计算机中的取余 Remainder）
```
#### 整除运算符//
取计算结果的最小整数，例如
```ruby
my_int_1 = 14
my_int_2 = 3
div_ints = my_int_1 // my_int_2 #4
my_float_1 = 5.4
my_float_2 = 12.0
floor_div_floats = my_float_2 // my_float_1 #2.0
```
#### 幂运算**
幂运算将一个数提升到另一个数的幂，使用双星号操作符（**）:
```ruby

```