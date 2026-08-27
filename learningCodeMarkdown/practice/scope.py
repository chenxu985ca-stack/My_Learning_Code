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
