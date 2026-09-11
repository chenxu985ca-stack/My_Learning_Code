# 三种方式的写法，这是一个数字的返回方法，参数设置为4，则返回1，2，3，4
def number_pattern1(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n <= 0:
        return "Argument must be an integer greater than 0."

    numbers = "1"

    for i in range(2, n + 1):
        numbers += ' ' + str(i)
    return ''.join(numbers)

# ---------------------------------------


def number_pattern2(n):
    result = "1"
    if isinstance(n, int):
        if n > 0:
            for i in range(2, n + 1):
                result += f" {i}"
            return result
        else:
            return "Argument must be an integer greater than 0."
    else:
        return "Argument must be an integer value."

# ---------------------------------------


def number_pattern(n):

    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n <= 0:
        return "Argument must be an integer greater than 0."

    numbers = []

    for i in range(1, n + 1):
        numbers.append(str(i))

    return " ".join(numbers)
