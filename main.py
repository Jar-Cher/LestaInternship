import random
import copy


# Task 1

# На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен
# нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

# Пример
# "Нормальное" решение. Просто, читаемо, быстро: одна операция деления и одна операция сравнения.
def is_even(value):
    return value % 2 == 0

# Решение
# "Математическое" решение: чётность последней цифры определяет чётность числа. Больше операций, менее читаемый код.
# Данный метод можно применить, если от value по каким-то причинам осталась только последняя цифра;
# это может произойти, например, в результате анонимизации исходных данных.
def is_even_custom(value):
    last_digit = value % 10
    # return last_digit % 2 тоже подойдёт
    return last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

def test_even():
    if not is_even_custom(42):
        print(f'Even test failed for number 42')
    if not is_even_custom(0):
        print(f'Even test failed for number 0')
    if is_even_custom(-11):
        print(f'Even test failed for number -11')
    for i in range(100500):
        number = random.randint(-1000, 1000)
        if is_even(number) != is_even_custom(number):
            print(f'Even test failed for number {number}')
    print("All even tests done")


# Task 2
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

#class buffer1():


# Task 3
# Реализация сортировки Хоара (quicksort)
# Худшее время - O(n^2)
# Среднее время - O(n*log(n))
# Лучшее время - O(n*log(n))
# array - сортируемый список, floor - индекс начального элемента, ceil - индекс последнего элемента
# floor и ceil указывают сортируемую часть списка array
def sort(array, floor, ceil):
    dif = ceil - floor
    # Пустой/одноэлементный список не сортируем.
    if dif < 2:
        return
    # Список из двух элементов можно отсортировать здесь и сейчас.
    if dif == 2:
        if array[floor] > array[ceil - 1]:
            swap(array, floor, ceil - 1)
            return
    # Вычисляем опорное значение - среднее арифметическое первого, центрального и последнего элементов списка.
    mid = (array[floor] + array[(floor + ceil) // 2] + array[ceil - 1]) // 3
    j = ceil - 1
    i = floor
    # Элементы больше опорного из начала списка меняются местами с элементами меньше опорного из конца.
    while i < j:
        if array[i] > mid:
            while array[j] > mid and i < j:
                j = j - 1
            swap(array, i, j)
        i = i + 1
    # array[j] - опорный элемент. Таким образом:
    # все элементы с меньшими индексами - не большего array[j];
    # все элементы с большими индексами - не меньшего array[j].
    # Далее, рекурсивно сортируем два подсписка относительно опорного элемента.
    sort(array, floor, j)
    sort(array, j, ceil)

def swap(array, first, second):
    array[first], array[second] = array[second], array[first]

def test_sort():
    for i in range(42):
        array_original = random.choices(range(42), k = 42)
        array_control = copy.deepcopy(array_original)
        array_control.sort()
        sort(array_original, 0, len(array_original))
        if array_control != array_original:
            print("Expected: " + array_control + "; Actual: " + array_original + "; Original")
    print("All sort tests done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_even()
    test_sort()