import unittest
from src.string_utils import print_string, check_case
from src.even_odd_gen import even_odd_generator
import io
import sys

class TestStringUtils(unittest.TestCase):
    # ... (Код для тестов, как мы обсуждали ранее)
    # Убедитесь, что импорт написан как from src.string_utils ...
    def test_print_string(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_string("Привіт, світе!")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Привіт, світе!\n")

        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_string(123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Помилка: аргумент має бути рядком (str).\n")

class TestGenerator(unittest.TestCase):
    # ... (Код для тестов)
    def test_even_odd_generator(self):
        gen = even_odd_generator()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")

if __name__ == '__main__':
    unittest.main()
