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
---

## 循环和序列
### 列表[`list`]
列表数据类型是一种**有序**的元素序列，可以包含字符串、数字，甚至其他列表。列表是可变的，并采用零基索引，即列表的第一个元素位于索引为零的位置。
#### 基本语法：
```ruby
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
cities[-1] # 'Tokyo'
```
#### `list()`函数
另一种创建列表的方法是使用 `list()` 构造函数。`list()` 构造函数用于将可迭代对象转换为列表，例如：
```ruby
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']
```
#### `len()`函数
要获取列表中元素的总数，可以使用 `len()` 函数，如下所示：
```ruby
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
```
#### `del`关键字
如果你想从列表中删除一个元素，可以使用 `del` 关键字，如下所示：
```ruby
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']
```
#### `in`
有时检查某个元素是否在列表中会很有帮助。为此，可以使用 `in` 关键字，如下所示：
```ruby
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```
#### `嵌套列表`
有时会遇到像这样嵌套的列表：
```ruby
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```
在这个示例中，我们有一个包含三种流行编程语言的嵌套列表。要访问该嵌套列表，需要使用索引 2，因为列表是基于零的索引：
```ruby
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']
```
然后要访问该嵌套列表中的'Python'，你需要使用索引0:
```ruby
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][0] # 'Rust'
```
### 列表的常用方法
#### `append()`
该方法用于将一个元素添加到列表的末尾。下面是一个使用 `append()` 方法将数字 6 添加到数字列表中的示例
```ruby
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]
```
如果你想在另一个列表的末尾添加一个列表，也可以使用 `append()` 方法，如下所示:
```ruby
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
```
这里要注意整个 `even_numbers` 列表是如何嵌套在 `numbers `列表中的。
#### `extend()`
但如果你想在数字列表末尾添加偶数列表中所有单独的数字，就可以使用 `extend()` 方法。
```ruby
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]
```
#### `insert()`
要在列表的特定位置插入元素，可以使用 `insert()` 方法。该方法接受两个参数：要插入新元素的位置索引以及要插入的元素本身。
```ruby
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

```
以上代码将在数字列表的第2个索引处插入数字2.5。
#### `remove()`
如果你想从列表中删除某个元素，可以使用 `remove()` 方法。`remove()` 方法需要传入要删除的元素的值作为参数:
```ruby
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]
```
需要注意的是，此方法只会删除第一个出现的项目，并非全部删除。
#### `pop()`
要删除列表中指定索引位置的元素，可以使用 `pop()` 方法，如下所示：
```ruby
numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned
```
如果未为 pop 方法指定元素，则会移除最后一个元素。
#### `clear()`
如果需要清空列表，可以使用 `clear()` 方法，如下所示：
```ruby
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []
```
#### `sort()`
接下来要介绍的方法是 `sort()` 方法。该方法用于就地排序元素。以下是一个将随机数字列表就地排序的示例
```ruby
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]
```
#### `sorted()`
与 `sort()` 方法不同，`sorted()` 函数适用于任何可迭代对象，并返回一个新的已排序列表，而不是修改原始列表。例如：
```ruby
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
```
`sort()` 方法和 `sorted()` 函数都支持可选的 `key` 和 `reverse` 参数。
#### `reverse()`
接下来要介绍的方法是 `reverse()` 方法。该方法会原地反转列表中的元素，具体如下：
```ruby
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]
```
#### `index()`
我们接下来要介绍的最后一种方法是`index`。该方法用于查找列表中某个元素首次出现的索引位置。以下是一个使用索引方法在`programming_languages`列表中查找`Java`的例子：
```ruby
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1
```
如果找不到该元素，Python 将抛出 ValueError：
```ruby
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""
```

### 元组(Tuples)
元组是一种Python数据类型，用于创建有序的值序列。元组可以包含混合的数据类型，例如：
```ruby
developer = ('Alice', 34, 'Rust Developer')
```
元组类似于列表，但列表是可变数据类型，而元组是不可变的。这意味着一旦创建了元组，其中的元素就无法被更改。
如果你尝试更新元组中的某个元素，将会得到一个 TypeError：
```ruby
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""
```
要访问元组中的元素，可以使用方括号表示法和索引号,如果需要从元组末尾开始访问元素，可以使用负索引。以下是一个使用负索引来访问元组倒数第二个元素的例子：
```ruby
developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34

numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4
```
如果你尝试传递一个超过或等于元组长度的索引号，就会收到类似这样的 IndexError 错误：
```ruby
numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
"""
```
#### tuple()构造函数
另一种创建元组的方法是使用 `tuple()` 构造函数，如下所示：
```ruby
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')
```
#### `in`
要检查某个项目是否在元组中，可以使用 `in` 关键字，如下所示：
```ruby
fruits = ('apple', 'bnana', 'orange', 'waterlemon')

'apple' in fruits # True
'pinapple' in fruits # False
```
#### 解包
和列表一样，从元组中解包元素：
```ruby
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'
```
如果需要从元组中收集剩余的元素，可以使用星号`*`操作符，如下所示：
```ruby
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']
```
与列表类似，你也可以使用切片操作符对元组进行切取，以提取其中的一部分。以下是一个将“pie”和“cookies”两个元素提取到单独元组中的示例：
```ruby
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')
```
#### 不可删除
如果需要从元组中删除某个元素，这是不可能的，因为元组是不可变的。因此，这个示例会产生错误：
```ruby
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
```
#### 什么情况下应该使用元组而不是列表？
如果你需要一个动态的元素集合，可以添加、删除和更新元素，那么应该使用列表。如果你知道要处理的是固定且不可变的数据集合，则应使用元组。
### 元组的常用方法
#### `count()`
我们首先介绍的方法是 `count()`。该方法用于确定某个元素在元组中出现的次数。以下是一个示例，用于检查字符串 "Rust" 在名为 programming_languages 的元组中出现了多少次,如果不存在，则显示为0，如果未向 `count()` 函数传递任何参数，Python 将抛出 TypeError：：
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2
programming_languages.count('JavaScript') # 0
```
#### `index()`
接下来要介绍的方法是 `index()` 方法。该方法用于查找元组中某个特定元素的位置索引。以下是一个使用 `index()` 方法查找字符串 "Java" 索引的示例,如果指定的项目未找到，Python 将抛出 ValueError：

：
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1
```

在下面这个例子中，我们指定了搜索字符串“Python”的起始位置。通过将数字3作为`index()`函数的第二个参数传入，我们指定从索引3开始搜索。由于元组中Python出现了两次，因此由于使用了可选的起始索引参数，`index()`函数会返回索引5，而不是索引2。
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5
```
你也可以给定一个搜索范围：
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2
```
#### `sorted()`
另一个常用于元组的函数是 `sorted()`函数。在上一课中，你学习了列表的 `sort()` 方法。那么，`sorted()` 函数可以应用于任何可迭代对象，包括元组。
```ruby
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]
```
`sorted()` 函数总是会创建一个包含已排序值的新列表。这与 `sort()` 方法不同，`sort()` 方法会就地对列表元素进行排序，并且不会返回新列表。

如果需要自定义可迭代对象的排序行为，可以使用可选的 reverse 和 key 参数。以下是一个使用 key 参数按元组中元素长度进行排序的例子：
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)
#按元素长度排序
# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```
如果你想创建一个按逆序排列的新值列表，可以使用 reverse 参数如下：
```ruby
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

### 循环
#### `for`循环
