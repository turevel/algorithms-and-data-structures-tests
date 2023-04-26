def sub(arr):
    initial_value = arr[0]

    for i in arr[1:]:
        initial_value -= i

    return initial_value


def div(a, b):
    if 0 in [a, b]:
        return "null"

    return a / b


def mul(arr):
    initial_value = 1

    for i in arr:
        initial_value *= i

    return initial_value


math = {
    "add": lambda arr: sum(arr),
    "sub": sub,
    "div": div,
    "mul": mul,
}


if __name__ == "__main__":
    add_result = math['add']([2, 3, 6, 9])
    sub_result = math['sub']([9, -4, 5, 1])
    div_result = math['div'](27, 3)
    mul_result = math['mul']([2, 3, 6, 9])

    print(add_result) # 20
    print(sub_result) # 7
    print(div_result) # 9
    print(mul_result) # 324
