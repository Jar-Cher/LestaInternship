import random

# Task 1

# На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен
# нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

# Пример
# "Нормальное" решение. Просто, читаемо, быстро: одна операция деления и одна операция сравнения.
def is_even(value):
    return value % 2 == 0

# Решение
# "Математическое" решение. Больше операций, менее читаемый код.
# Данный метод можно применить, если от исходных данных (value) по каким-то причинам осталась только последняя цифра.
def is_even_custom(value):
    last_digit = value % 10
    # return last_digit % 2 тоже подойдёт
    return last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

def test_even():
    if not is_even_custom(42):
        print(f'Custom even test failed for number 42')
    if not is_even_custom(0):
        print(f'Custom even test failed for number 0')
    if is_even_custom(-11):
        print(f'Custom even test failed for number -11')
    for i in range(100500):
        number = random.randint(-1000, 1000)
        if is_even(number) != is_even_custom(number):
            print(f'Custom even test failed for number {number}')
    print("All even tests done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_even()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
