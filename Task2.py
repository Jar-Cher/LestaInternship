from abc import ABC, abstractmethod
from collections import deque

# Task 2
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.


# Абстрактный базовый класс, на всякий случай.
class CustomBuffer(ABC):
    @abstractmethod
    def __init__(self, size):
        self._size = size

    @abstractmethod
    def append(self, element):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
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
        # Индекс элемента, который будет "удалён" из буфера
        self.__index_pop = 0
        self.__elements_stored = 0

    def append(self, element):
        self.__list[self.__index_add] = element
        if self.__elements_stored == self._size:
            self.__index_pop = (self.__index_pop + 1) % self._size
        else:
            self.__elements_stored += 1
        self.__index_add = (self.__index_add + 1) % self._size

    def pop(self):
        if self.__elements_stored == 0:
            raise IndexError
        self.__elements_stored -= 1
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
        self.__deque = deque(maxlen = size)

    def append(self, element):
        self.__deque.append(element)

    def pop(self):
        return self.__deque.popleft()

    def get_buffer(self):
        return list(self.__deque)