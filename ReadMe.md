### 这是一个我自己记录学习python的文件夹。

*作为一个学了三年Java的大专生，我深深的为自己所学之浅感到遗憾*

#### 为什么想学？
因为在专科时期根本就没有学习下来任何东西，仅仅只了解了皮毛，可是在这个AI时代，我又深感代码、计算机语言的重要性，于是我发自内心的想学习 Python。

---

#### 为什么是 Python？
>因为我听说Python是最优美的语言，而且易用性、易读性很强，与英语也有强相关。

借由学习Python这一门计算机语言，往后我可以学习其他计算机语言，例如Java，C，C++，汇编

---

#### 到目前为止，学习到哪个阶段了？
刚刚入门，自己写了几个小的入门程序，例如闹钟、数字炸弹、摄氏度转华氏度。
```ruby javascript {.line-numbers}
#闹钟程序
import time

my_time = int(input("Type your time: "))

for x in range(my_time, 0, -1):
    second = x % 60
    minuts = int((x / 60) % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minuts:02}:{second:02}")
    time.sleep(1)

print("Time's UP!!!!")
```
```ruby javascript {,highlight=1-12}
#温度转换器
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
```
让我感受到庆幸的是现在的AI功能十分强大，我用AI coding，为我现在工作的公司，写了两个网站，
**一个是：**[西湖巴尔产品手册网站](http://cunxiaziyou.cn/biomaterial/index.html) ；
我也为它搭建好了后台：[西湖巴尔产品手册网站后台](http://cunxiaziyou.cn/biomaterial/admin) ，这个项目是做的算比较完整的，前台后台都搭建了，数据库是用的supabase。
**另一个是：**[西湖巴尔销售助手](https://chenxu985ca-stack.github.io/xihu_sales/index.html)； 
这个网站仅仅是有一个静态展示网站，没有做数据库，功能方面有查询产品、添加报价、打印报价、复制报价。

---

#### 不是有AI了吗？怎么还想着自己要学
也是由于AI的出现，让我意识到，我必须学会并掌握编程，即使可以有AI帮着我写代码，但是我必须也要自己看得懂，所以Python成了使用AI、掌握AI的不可或缺的一环。

---

#### 我发现我也很喜欢写这种Markdown文件
这样写出来的文字很优美，既有颜色，还有样式，要是最后能够切换字体就更好了,我喜欢苹果的字体。

学习Python的笔记 [^1]
[^1]:学习Python笔记

