import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):    
        self.assertTrue(is_prime(5)) 
    
    def test_if_foo_prime(self):
        self.assertFalse(is_prime('foo'))

    def test_if_two_prime(self):
        self.assertFalse(is_prime(2))

    def test_if_one_prime(self):
        self.assertFalse(is_prime(1))

    def test_of_neg_one_prime(self):
        self.assertFalse(is_prime(-1))

if __name__ == '__main__':
    unittest.main()
