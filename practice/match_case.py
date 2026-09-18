# match case 缩略if，elif，else

# 可行，但可读性不够好，看起来呆板

def day_of_week(day):

    if day == '1':
        return "周一"
    elif day == '2':
        return "周二"
    elif day == '3':
        return "周三"
    elif day == '4':
        return "周四"
    elif day == '5':
        return "周五"
    elif day == '6':
        return "周六"
    elif day == '7':
        return "周天"
    else:
        return "请输入正确的值"


print(day_of_week("3"))


# 使用match之后，会简略许多

def day_of_week1(day):
    match day:
        case '1':
            return '周一'
        case '2':
            return '周二'
        case '3':
            return '周三'
        case '4':
            return '周四'
        case '5':
            return '周五'
        case '6':
            return '周六'
        case '7':
            return '周天'
        case _:
            return '请输入正确的值'


print(day_of_week1('3'))


# 让我们看看另外的一个例子
def is_weekend(day):
    match day:
        case 'sunday':
            return True
        case 'monday':
            return False
        case 'tuseday':
            return False
        case 'wednesday':
            return False
        case 'thursday':
            return False
        case 'friday':
            return False
        case 'saturday':
            return True
        case _:
            return '请输入正确的值'


print(is_weekend('saturday'))


# 上面的例子可以简写为以下代码：
# 非常简洁优美

def is_weekend(day):
    match day:
        case 'sunday' | 'saturday':
            return True
        case 'monday' | 'tuseday' | 'wednesday' | 'thursday' | 'friday':
            return False
        case _:
            return '请输入正确的值'


print(is_weekend('tuseday'))
