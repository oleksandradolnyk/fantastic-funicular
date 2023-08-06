import unittest
from functions import formatted_name


class TestFormattedName(unittest.TestCase):

    def test_full_name(self):
        self.assertEqual(formatted_name("Mykhail", "Shevchuk", "Ivanovych"), "Mykhail Ivanovych Shevchuk")

    def test_with_two_values(self):
        self.assertEqual(formatted_name("Mykhail", "Shevchuk"), "Mykhail Shevchuk")

    def test_without_values(self):
        with self.assertRaises(TypeError) as exp:
            formatted_name()
        self.assertEqual(str(exp.exception), "formatted_name() missing 2 required positional arguments: 'first_name' "
                                             "and 'last_name'")

    def test_with_middle_only(self):
        with self.assertRaises(TypeError) as exp:
            formatted_name(middle_name="Ivanovych")
        self.assertEqual(str(exp.exception), "formatted_name() missing 2 required positional arguments: 'first_name' "
                                             "and 'last_name'")

    def test_without_one_value(self):
        with self.assertRaises(TypeError) as exp:
            formatted_name(first_name="Mykhail")
        self.assertEqual(str(exp.exception), "formatted_name() missing 1 required positional argument: 'last_name'")

        with self.assertRaises(TypeError) as exp:
            formatted_name(last_name="Shevchuk")
        self.assertEqual(str(exp.exception), "formatted_name() missing 1 required positional argument: 'first_name'")

    def test_non_string_value(self):
        with self.assertRaises(TypeError) as exp:
            formatted_name(123, 123)
        self.assertEqual(str(exp.exception), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_middle_name_as_integer(self):
        with self.assertRaises(TypeError) as exp:
            formatted_name("Mykhail", "Shevchuk", 123)
        self.assertEqual(str(exp.exception), "object of type 'int' has no len()")
