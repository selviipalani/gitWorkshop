import unittest
import sys

sys.path.append("../src")
import fizz_buzz
# from src import fizz_buzz


class TestStringMethods(unittest.TestCase):

    def test_fizz_buzz_main(self):
        self.assertEqual(fizz_buzz.main(), [])
        print("executing fb main")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
