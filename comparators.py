import random


def counting(f):
    def counted(*args, **kwargs):
        counted.calls += 1
        return f(*args, **kwargs)
    counted.calls = 0
    return counted


@counting
def user_choice(item1, item2):
    print("Comparison #" + str(user_choice.calls))
    print("1: " + item1)
    print("2: " + item2)

    while True:
        choice = input("Which do you prefer?\n")
        if choice in {"1", "2"}: break

    print()
    return [item1, item2][int(choice)-1]


@counting
def random_choice(item1, item2):
    return random.choice((item1, item2))


@counting
def longer_of(item1, item2):
    return max((item1, item2), key=lambda item: len(item))


@counting
def bigger_int(item1, item2):
    return max((item1, item2), key=lambda item: int(item))