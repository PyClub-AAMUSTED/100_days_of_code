import unittest
import sys
import os

# Add the parent directory of 'intermediate' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../intermediate')))

from Grandkojo.primeNumberCheck import prime_number_check

class TestPrimeNumberCheck(unittest.TestCase):

    def test_valid_primes(self):
        self.assertEqual(prime_number_check(2), "Prime Number")
        self.assertEqual(prime_number_check(3), "Prime Number")
        self.assertEqual(prime_number_check(11), "Prime Number")

    def test_non_primes(self):
        self.assertEqual(prime_number_check(4), "Not a prime number")
        self.assertEqual(prime_number_check(10), "Not a prime number")
        self.assertEqual(prime_number_check(100), "Not a prime number")

    def test_invalid_inputs(self):
        self.assertEqual(prime_number_check(1), "Invalid")
        self.assertEqual(prime_number_check(0), "Invalid")
        self.assertEqual(prime_number_check(-7), "Invalid")
        self.assertEqual(prime_number_check(10.5), "Invalid")
        self.assertEqual(prime_number_check("string"), "Invalid")

if __name__ == "__main__":
    unittest.main()
