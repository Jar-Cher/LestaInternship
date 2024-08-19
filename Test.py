from copy import deepcopy
from random import choices, randint, random
from Task1 import is_even, is_even_custom
from Task2 import CustomBuffer, Buffer1, Buffer2
from Task3 import sort
import unittest


class Test(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even_custom(42))
        self.assertTrue(is_even_custom(0))
        self.assertFalse(is_even_custom(-11))
        for i in range(100500):
            number = randint(-1000, 1000)
            self.assertEqual(is_even(number), is_even_custom(number))
        print("All even tests done")

    def test_buffer(self):
        test_size = randint(1, 42)
        buf1 = Buffer1(test_size)
        buf2 = Buffer2(test_size)
        self.assertIsInstance(buf1, CustomBuffer)
        self.assertIsInstance(buf2, CustomBuffer)
        for i in range(283):
            if random() < 0.7:
                test_additive = randint(1, 42)
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
                self.assertEqual(pop1, pop2)
            self.assertEqual(buf1.get_buffer(), buf2.get_buffer())
        print("All buffer tests done")

    def test_sort(self):
        list_original = [-1, 100, 42, 134, 9000, 100500, 64, -5, 4]
        sort(list_original, 0, len(list_original))
        self.assertEqual(list_original, [-5, -1, 4, 42, 64, 100, 134, 9000, 100500])
        for i in range(42):
            list_original = choices(range(randint(1, 1000)), k=42)
            list_control = deepcopy(list_original)
            list_control.sort()
            sort(list_original, 0, len(list_original))
            self.assertEqual(list_control, list_original)
        print("All sort tests done")
