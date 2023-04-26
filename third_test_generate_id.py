from random import randint

CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"


def generate_id():
    _id = ""

    for i in range(16):
        if i > 0 and i % 4 == 0:
            _id += "-"

        index = randint(0, len(CHARACTERS) -1)
        _id += CHARACTERS[index]

    return _id


if __name__ == "__main__":
    _id = generate_id()

    print(_id) # Exemplo: k7er-c4lb-e1od-kwqp
