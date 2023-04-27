from functools import reduce


def arg_validator(arr):
    if not isinstance(arr, list):
        raise ValueError('Você precisa informar uma lista!')

    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]


def add(arr):
    validate = arg_validator(arr)

    return validate \
        if validate is not None \
        else reduce(lambda a, b: a + b, arr)


def sub(arr):
    validate = arg_validator(arr)

    return validate \
        if validate is not None \
        else reduce(lambda a, b: a - b, arr)


def div(a, b):
    if b == 0:
        raise ValueError('Não se pode fazer divisão por 0!')

    return a / b


def mul(arr):
    validate = arg_validator(arr)

    return validate \
        if validate is not None \
        else reduce(lambda a, b: a * b, arr)


math = {
    "add": add,
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
