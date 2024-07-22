#file to test function

import unittest
from is_prime import is_prime


class Testing(unittest.TestCase):
    

    #pass
    def test_always_passes(self):
        self.assertTrue(True)
    #fail
    def test_always_fails(self):
        self.assertFalse(False)

    #Non-prime numbers (false)
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))

    #Prime numbers (True)
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
    
    #edge cases
    def test_edge_cases(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(None))



if __name__ == "__main__":
    unittest.main()