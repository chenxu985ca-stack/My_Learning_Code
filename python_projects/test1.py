def number_pattern(n):
    number = "1"
    if isinstance(n, int):
        if n > 0:
            for i in range(2, n + 1):
                number += f" {i}"
            return number
        else:
            return "Argument must be an integer greater than 0."
    return "Argument must be an integer value."


print(number_pattern(1))
