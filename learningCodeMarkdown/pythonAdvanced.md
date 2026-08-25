# Python 进阶
## 函数
函数是可重复使用的代码片段，当你调用它们时就会执行。Python 提供了内置函数，包括 `print()`、`input()`。
### 自定义函数
你也可以编写自己的自定义函数。为此，使用 `def` 关键字，后跟你想给函数起的名字、一对括号和冒号。然后在新的一行中写入该函数应执行的代码。函数执行的代码也称为函数体。例如：
```ruby
def hello():
    print('Hello World')
```
调用时,需使用其名称后跟一对括号进行调用：
```ruby
hello() # Hello World
```
#### 参数
我们还可以在函数中插入参数，例如：
```ruby
def calculate_sum(a, b):
    print(a + b)
#这是一个计算两个数字之和的简单函数
```
我们的函数 calculate_sum 在括号中包含 `a` 和 `b`，它们之间用逗号分隔。这些被称为参数（`parameters`）。可以把参数想象成占位符变量，它们在调用函数时作为“插槽”来接收你传入的值。
#### 传参
要使用参数，必须传入“参数”。参数是指调用函数时传递给它的值。
```ruby
calculate_sum(3, 1) # 打印台输出：4
```
如果未传入正确数量的参数调用该函数，将会得到 TypeError：
```ruby
calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
```
#### return
函数还使用一个特殊的返回关键字来退出函数并返回值。如果你没有显式使用 return，Python 会默认返回 None。例如：
```ruby
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```
你可以看到，`calculate_sum` 函数会打印 `a` 和 `b` 的和，但并没有显式地返回任何值。因此，当我们把它的结果赋给 `my_sum` 时，实际的值是 `None`。要解决这个问题，可以使用 `return` 关键字来返回结果：
```ruby
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4

```
现在，`calculate_sum` 返回 `a` 和 `b` 的和，并将结果存储在 `my_sum` 中。

---

## 作用域
为了正确确定作用域，Python 遵循 LEGB 规则，其含义如下：

- Local scope (L): Variables defined inside functions.
局部作用域（L）：在函数内部定义的变量。

- Enclosing scope (E): Variables defined in enclosing or nested functions.
外层作用域（E）：在外部或嵌套函数中定义的变量。

- Global scope (G): Variables defined at the top level of a file.
全局作用域（G）：在文件顶层定义的变量。

- Built-in scope (B): Names that Python provides, such as print, str, type, and isinstance.
内置作用域（B）：Python 提供的名称，例如 `print`、`str`、`type` 和 `isinstance`。

### 局部作用域
局部作用域意味着在函数内部声明的变量只能在该函数内部访问。
```ruby
def my_func():
    my_var = 10
    print(my_var)
```
在这种情况下，my_func 函数拥有自己的作用域，无法从函数外部访问。调用 my_func 会输出 10，但若在函数外部打印 my_var 就会导致 NameError 错误：
```ruby
def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

print(my_var) # NameError: name 'my_var' is not defined
```

### 封闭作用域
封闭作用域意味着，嵌套在另一个函数内部的函数可以访问其所在函数中的变量。
```ruby
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!
```
在这个例子中，内层函数 `inner_func` 可以自由访问外层函数 `outer_func` 中定义的 `msg` 变量。但请注意，外层函数无法访问任何嵌套函数内部定义的变量：
```ruby
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined
```
这是因为 `res` 在 `inner_func` 中是局部作用域的。另外请注意，`outer_func` 会在 `inner_func` 被调用之前尝试打印 `res`。
一种解决方案是在外层作用域（即 `outer_func` 内）将 `res` 初始化为空字符串。然后在内层函数 `inner_func` 中，使用 `nonlocal` 关键字将 `res` 设为非局部变量：
```ruby
def outer_func():
    msg = 'Hello there!'
    res = ""  # 在外层作用域中声明res

    def inner_func():
        nonlocal res  # 允许修改外部的res
        res = 'How are you?'
        print(msg)  # 从 outer_func() 中访问 msg   

    inner_func()
    print(res)  # 现在 res 已可访问且已被修改

outer_func()

# 输出:
# Hello there!
# How are you?
```
### 全局作用域
全局作用域指的是在任何函数外部声明的变量，可以在程序中的任何位置访问。在这里，`my_var` 可以在任何地方被访问，即使是在它未定义的函数内部：
```ruby
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100
```
如果你想让函数内部定义的局部变量变为全局可访问，可以使用 global 关键字：
```ruby javascript {highlight=4}
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 现在是一个全局变量，可以在程序中的任何地方被访问
print(my_var_2) # 10
```
你也可以使用全局关键字来修改全局变量：
```ruby
my_var = 10  # 全局变量

def change_var():
    global my_var  # 允许修改全局变量
    my_var = 20

change_var()

print(my_var)  # my_var 现在已在全局范围内被修改为 20
```
### 内置作用域
内置作用域包含 Python 提供的名称，包括内置函数、模块和关键字。这些名称在程序的任何位置都可以使用，直接调用即可：
```ruby
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
```