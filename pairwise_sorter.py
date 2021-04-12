import comparators
import selectors
import random


def main():
    with open("list_of_values.txt") as f:
        unsorted = f.read().splitlines()
        random.shuffle(unsorted)

    unsorted = [str(x) for x in range(88)]
    random.shuffle(unsorted)

    better_of = comparators.bigger_int
    top_k = get_top_k(unsorted, 10, better_of=better_of)
    print(top_k)
    print(str(better_of.calls) + " comparisons")


"""
    better_of: comparator -- takes 2 items and returns the better one
        (1) user_choice
        (2) random_choice
        (3) longer_of
        (4) bigger_int
    top: selector -- takes a list and returns the top k best items
        (1) quicktop
        (2) mergetop
        (3) bubbletop
        (4) touneytop
"""
def get_top_k(unsorted, k, 
              better_of=comparators.user_choice,
              top=selectors.tourneytop):
    return top(unsorted, k, better_of)


if __name__ == "__main__":
    main()