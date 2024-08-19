# Task 3
# Реализация сортировки Хоара (quicksort)
# Худшее время - O(n^2)
# Среднее время - O(n*log(n))
# Лучшее время - O(n*log(n))
# array - сортируемый список, floor - индекс начального элемента, ceil - индекс последнего элемента
# floor и ceil указывают сортируемую часть списка list


def sort(sort_list, floor, ceil):
    dif = ceil - floor
    # Пустой/одноэлементный список не сортируем.
    if dif < 2:
        return
    # Список из двух элементов можно отсортировать здесь и сейчас.
    if dif == 2:
        if sort_list[floor] > sort_list[ceil - 1]:
            swap(sort_list, floor, ceil - 1)
            return
    # Вычисляем опорное значение - среднее арифметическое первого, центрального и последнего элементов списка.
    mid = (sort_list[floor] + sort_list[(floor + ceil) // 2] + sort_list[ceil - 1]) // 3
    j = ceil - 1
    i = floor
    # Элементы больше опорного из начала списка меняются местами с элементами меньше опорного из конца.
    while i < j:
        if sort_list[i] > mid:
            while sort_list[j] > mid and i < j:
                j -= 1
            swap(sort_list, i, j)
        i += 1
    # list[j] - опорный элемент. Таким образом:
    # все элементы с меньшими индексами - не большего list[j];
    # все элементы с большими индексами - не меньшего list[j].
    # Далее, рекурсивно сортируем два подсписка относительно опорного элемента.
    sort(sort_list, floor, j)
    sort(sort_list, j, ceil)

def swap(swap_list, first, second):
    swap_list[first], swap_list[second] = swap_list[second], swap_list[first]