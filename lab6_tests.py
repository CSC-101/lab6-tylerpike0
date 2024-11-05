import data
import lab6
import unittest

from data import Book



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_selection_sort_books_1(self):
        books = [
            Book(["Joline"], "Night"),
            Book(["Joe"], "Midnight"),
            Book(["Joey"], "Midday")

        ]
        expected = [
            Book(["Joey"], "Midday"),
            Book(["Joe"], "Midnight"),
            Book(["Joline"], "Night")
        ]
        actual = books.copy()
        lab6.selection_sort_books(actual)
        self.assertEqual(expected, actual)

    def test_selection_sort_books_2(self):
        books = [

        ]
        expected = [

        ]
        actual = books.copy()
        lab6.selection_sort_books(actual)
        self.assertEqual(expected, actual)


    # Part 2

    def test_swap_case_1(self):
        input = "Cal Poly San Luis Obispo"
        expected = "cAL pOLY sAN lUIS oBISPO"
        actual = lab6.swap_case(input)
        self.assertEqual(expected,actual)

    def test_swap_case_2(self):
        input = "he4EOV4!*&@"
        expected = "HE4eov4!*&@"
        actual = lab6.swap_case(input)
        self.assertEqual(expected,actual)

    # Part 3

    def test_str_translate_1(self):
        input_string = "Cal Poly San Luis Obispo"
        old_char = "s"
        new_char = "x"
        expected = "Cal Poly San Luix Obixpo"
        actual = lab6.str_translate(input_string, old_char, new_char)
        self.assertEqual(expected,actual)

    def test_str_translate_2(self):
        input_string = "aababcabcdabcdeabcdef"
        old_char = "b"
        new_char = "*"
        expected = "aa*a*ca*cda*cdea*cdef"
        actual = lab6.str_translate(input_string, old_char, new_char)
        self.assertEqual(expected,actual)

    # Part 4

    def test_histogram_1(self):
        input = "hi hello hi bye hi hello"
        expected = {
            "hi": 3,
            "hello": 2,
            "bye": 1
        }
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)

    def test_histogram_2(self):
        input = "burrito sandwich pizza sandwich sandwich pizza soup"
        expected = {
            "burrito": 1,
            "sandwich": 3,
            "pizza": 2,
            "soup": 1
        }
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
