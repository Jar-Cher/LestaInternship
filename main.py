import random

def is_even(value):
    return value % 2 == 0

def is_even_custom(value):
    last_digit = value % 10
    return last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

def test_even():
    for i in range(100500):
        number = random.randint(-1000, 1000)
        if is_even(number) != is_even_custom(number):
            print(f'Custom even test failed for number {number}')
    print("All even tests done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_even()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
