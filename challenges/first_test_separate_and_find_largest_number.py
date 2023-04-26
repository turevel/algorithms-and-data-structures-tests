if __name__ == "__main__":
    arr = ["a", 10, "b", "hola", 122, 15]
    strings, numbers = [], []

    for i in arr:
        if isinstance(i, int):
            numbers.append(i)
            continue

        strings.append(i)

    print("Strings no array: ", strings) # Strings no array:  ['a', 'b', 'hola']
    print("Números no array: ", numbers) # Números no array:  [10, 122, 15]
    print("Maior número: ", max(numbers)) # Maior número:  122
