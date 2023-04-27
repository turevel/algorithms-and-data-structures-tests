from functools import reduce


def list_validator(arr):
    if not isinstance(arr, list):
        raise TypeError('Você precisa informar uma lista!')

    if not all([isinstance(i, (int, float)) for i in arr]):
        raise ValueError('Todos os valores precisam ser numéricos!')

    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]


def exec(arr, reduce_lambda):
    validate = list_validator(arr)

    return validate \
        if validate is not None \
        else reduce(reduce_lambda, arr)


def div(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Ambos os valores precisam ser numéricos!')

    if b == 0:
        raise ZeroDivisionError('Não é possível dividir por 0!')

    return a / b


math = {
    "add": lambda arr: exec(arr, lambda a, b: a + b),
    "sub": lambda arr: exec(arr, lambda a, b: a - b),
    "div": div,
    "mul": lambda arr: exec(arr, lambda a, b: a * b),
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
