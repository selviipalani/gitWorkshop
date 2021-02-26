# lib imports
import unittest
import sys

sys.path.append("../src")
import fizz_buzz


class TestFizzBuzzMethods(unittest.TestCase):

    def test_fizz_buzz(self):
        three, five, fifteen = fizz_buzz.fizz_buzz(1000)
        
        self.assertEqual(len(three), 333)
        self.assertEqual(len(five), 199)
        self.assertEqual(len(fifteen), 66)
    
    def test_fizz_buzz_neg(self):
        three, five, fifteen = fizz_buzz.fizz_buzz(-1)
        self.assertEqual(len(three), 0)
        self.assertEqual(len(five), 0)
        self.assertEqual(len(fifteen), 0)

    def test_fizz_buzz_zero(self):
        three, five, fifteen = fizz_buzz.fizz_buzz(0)
        self.assertEqual(len(three), 0)
        self.assertEqual(len(five), 0)
        self.assertEqual(len(fifteen), 0)

if __name__ == '__main__':
    unittest.main()
