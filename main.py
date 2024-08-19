import abc
import collections
import copy
import random


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

# Абстрактный базовый класс, на всякий случай.
class CustomBuffer(abc.ABC):
    @abc.abstractmethod
    def __init__(self, size):
        self._size = size

    @abc.abstractmethod
    def append(self, element):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    @abc.abstractmethod
    def get_buffer(self):
        pass

# Реализация №1
# В основе - список.
# Достоинства в отличие от реализации №2:
# 1. Можно достучаться до уже "удалённых", но ещё не затёртых элементов;
# 2. Длину списка изменить проще, чем read-only deque.maxlen.
# Недостаток - сложность кода.
class Buffer1(CustomBuffer):
    def __init__(self, size):
        super().__init__(size)
        self.__list = [None] * size
        # Индекс элемента, в который будет вставлен новый элемент
        self.__index_add = 0
        # Индекс элемента, который будет выделен из
        self.__index_pop = 0
        self.__elements_stored = 0

    def append(self, element):
        self.__list[self.__index_add] = element
        if self.__elements_stored == self._size:
            self.__index_pop = (self.__index_pop + 1) % self._size
        else:
            self.__elements_stored = self.__elements_stored + 1
        self.__index_add = (self.__index_add + 1) % self._size

    def pop(self):
        if self.__elements_stored == 0:
            raise IndexError
        self.__elements_stored = self.__elements_stored - 1
        element = self.__list[self.__index_pop]
        self.__index_pop = (self.__index_pop + 1) % self._size
        return element

    def get_buffer(self):
        return [self.__list[(i + self.__index_pop) % self._size] for i in range(self.__elements_stored)]

# Реализация №2
# Обёртка вокруг deque. Достоинства решения:
# 1. Не изобретаем велосипед;
# 2. Можно просто обернуть прочие методы deque и, например, реализовать LIFO.
# Недостаток - свойственная deque большая трата памяти.
class Buffer2(CustomBuffer):
    def __init__(self, size):
        super().__init__(size)
        self.__deque = collections.deque(maxlen = size)

    def append(self, element):
        self.__deque.append(element)

    def pop(self):
        return self.__deque.popleft()

    def get_buffer(self):
        return list(self.__deque)

def test_buffer():
    test_size = random.randint(1, 42)
    buf1 = Buffer1(test_size)
    buf2 = Buffer2(test_size)
    if not isinstance(buf1, CustomBuffer):
        print("buf1 is not a CustomBuffer")
    if not isinstance(buf2, CustomBuffer):
        print("buf2 is not a CustomBuffer")
    for i in range(283):
        if random.random() < 0.7:
            test_additive = random.randint(1, 42)
            buf1.append(test_additive)
            buf2.append(test_additive)
        else:
            try:
                pop1 = buf1.pop()
            except IndexError:
                pop1 = None
            try:
                pop2 = buf2.pop()
            except IndexError:
                pop2 = None
            if pop1 != pop2:
                print("Buffer1 popped " + str(pop1) + ", but Buffer2 popped " + str(pop2))
        if buf1.get_buffer() != buf2.get_buffer():
            print("Expected: " + str(buf1.get_buffer()) + "; Actual: " + str(buf2.get_buffer()))
    print("All buffer tests done")


# Task 3
# Реализация сортировки Хоара (quicksort)
# Худшее время - O(n^2)
# Среднее время - O(n*log(n))
# Лучшее время - O(n*log(n))
# array - сортируемый список, floor - индекс начального элемента, ceil - индекс последнего элемента
# floor и ceil указывают сортируемую часть списка list
def sort(list, floor, ceil):
    dif = ceil - floor
    # Пустой/одноэлементный список не сортируем.
    if dif < 2:
        return
    # Список из двух элементов можно отсортировать здесь и сейчас.
    if dif == 2:
        if list[floor] > list[ceil - 1]:
            swap(list, floor, ceil - 1)
            return
    # Вычисляем опорное значение - среднее арифметическое первого, центрального и последнего элементов списка.
    mid = (list[floor] + list[(floor + ceil) // 2] + list[ceil - 1]) // 3
    j = ceil - 1
    i = floor
    # Элементы больше опорного из начала списка меняются местами с элементами меньше опорного из конца.
    while i < j:
        if list[i] > mid:
            while list[j] > mid and i < j:
                j = j - 1
            swap(list, i, j)
        i = i + 1
    # list[j] - опорный элемент. Таким образом:
    # все элементы с меньшими индексами - не большего list[j];
    # все элементы с большими индексами - не меньшего list[j].
    # Далее, рекурсивно сортируем два подсписка относительно опорного элемента.
    sort(list, floor, j)
    sort(list, j, ceil)

def swap(list, first, second):
    list[first], list[second] = list[second], list[first]

def test_sort():
    list_original = [-1, 100, 42, 134, 9000, 100500, 64, -5, 4]
    sort(list_original, 0, len(list_original))
    if list_original != [-5, -1, 4, 42, 64, 100, 134, 9000, 100500]:
        print("Expected: [-5, -1, 4, 42, 64, 100, 134, 9000, 100500]; Actual: " + str(list_original))
    for i in range(42):
        list_original = random.choices(range(random.randint(1, 1000)), k = 42)
        list_control = copy.deepcopy(list_original)
        list_control.sort()
        sort(list_original, 0, len(list_original))
        if list_control != list_original:
            print("Expected: " + list_control + "; Actual: " + list_original)
    print("All sort tests done")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_even()
    test_buffer()
    test_sort()