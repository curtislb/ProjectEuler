#!/usr/bin/env python3

"""test_primes.py

Unit test for the 'primes' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.primes as prime


class TestPrimes(unittest.TestCase):
    def test_count_prime_factors(self) -> None:
        self.assertEqual(prime.count_prime_factors(1), 0)
        self.assertEqual(prime.count_prime_factors(1, []), 0)
        self.assertEqual(prime.count_prime_factors(2), 1)
        self.assertEqual(prime.count_prime_factors(2, [2]), 1)
        self.assertEqual(prime.count_prime_factors(3), 1)
        self.assertEqual(prime.count_prime_factors(3, [2, 3]), 1)
        self.assertEqual(prime.count_prime_factors(3, [2, 3, 5]), 1)
        self.assertEqual(prime.count_prime_factors(4), 1)
        self.assertEqual(prime.count_prime_factors(4, [2]), 1)
        self.assertEqual(prime.count_prime_factors(4, [2, 3, 5]), 1)
        self.assertEqual(prime.count_prime_factors(12), 2)
        self.assertEqual(prime.count_prime_factors(12, [2, 3]), 2)
        self.assertEqual(prime.count_prime_factors(12, [2, 3, 5, 7, 11]), 2)
        self.assertEqual(
            prime.count_prime_factors(30, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
            3)
        self.assertEqual(prime.count_prime_factors(360), 3)
        self.assertEqual(prime.count_prime_factors(1327), 1)
        self.assertEqual(prime.count_prime_factors(4200), 4)
        
    def test_is_prime(self) -> None:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}
        for n in range(2, 59):
            self.assertEqual(prime.is_prime(n), n in primes)
        self.assertFalse(prime.is_prime(993))
        self.assertFalse(prime.is_prime(995))
        self.assertTrue(prime.is_prime(997))
        self.assertFalse(prime.is_prime(999))
        self.assertFalse(prime.is_prime(10006719))
        self.assertTrue(prime.is_prime(10006721))
        self.assertFalse(prime.is_prime(10006723))
        self.assertFalse(prime.is_prime(2097151))
        self.assertTrue(prime.is_prime(2147483647))
        self.assertFalse(prime.is_prime(4294967295))
        
    def test_prime_factorization(self) -> None:
        self.assertEqual(prime.prime_factorization(2), [[2, 1]])
        self.assertEqual(prime.prime_factorization(3), [[3, 1]])
        self.assertEqual(prime.prime_factorization(4), [[2, 2]])
        self.assertEqual(prime.prime_factorization(5), [[5, 1]])
        self.assertEqual(prime.prime_factorization(6), [[2, 1], [3, 1]])
        self.assertEqual(prime.prime_factorization(12), [[2, 2], [3, 1]])
        self.assertEqual(prime.prime_factorization(2903), [[2903, 1]])
        self.assertEqual(
            prime.prime_factorization(61740),
            [[2, 2], [3, 2], [5, 1], [7, 3]])
        self.assertEqual(
            prime.prime_factorization(4928693),
            [[7, 1], [11, 3], [23, 2]])
        self.assertEqual(
            prime.prime_factorization(169165232),
            [[2, 4], [17, 1], [313, 1], [1987, 1]])
        self.assertEqual(
            prime.prime_factorization(74435892358158),
            [[2, 1], [3, 3], [29, 1], [3049, 2], [5113, 1]])
        
    def test_prime(self) -> None:
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        for i, n in enumerate(p_nums):
            self.assertEqual(prime.prime(i + 1), n)
        self.assertEqual(prime.prime(74), 373)
        self.assertEqual(prime.prime(225), 1427)
        self.assertEqual(prime.prime(538), 3881)

    def test_primes(self) -> None:
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        for i in range(1, len(p_nums) + 1):
            self.assertCountEqual(prime.primes(i), p_nums[:i])
        self.assertEqual(prime.primes(168)[-1], 997)

    def test_primes_up_to(self) -> None:
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97]
        for n in range(2, 100):
            self.assertCountEqual(
                prime.primes_up_to(n),
                filter(lambda x: x <= n, p_nums))
        self.assertEqual(len(prime.primes_up_to(1000)), 168)


if __name__ == '__main__':
    unittest.main()
