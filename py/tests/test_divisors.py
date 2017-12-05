"""test_divisors.py

Unit test for the 'divisors' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.divisors as divs


class TestDivisors(unittest.TestCase):
    def test_count_divisors(self) -> None:
        div_cts = [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6]
        for i, n in enumerate(div_cts):
            self.assertEqual(divs.count_divisors(i + 1), n)
        self.assertEqual(divs.count_divisors(4200), 48)
        self.assertEqual(divs.count_divisors(15485863), 2)

    def test_count_divisors_up_to(self) -> None:
        self.assertEqual(divs.count_divisors_up_to(0), [0])
        self.assertEqual(divs.count_divisors_up_to(1), [0, 1])
        self.assertEqual(divs.count_divisors_up_to(2), [0, 1, 2])
        self.assertEqual(divs.count_divisors_up_to(3), [0, 1, 2, 2])
        self.assertEqual(divs.count_divisors_up_to(4), [0, 1, 2, 2, 3])
        self.assertEqual(
            divs.count_divisors_up_to(43),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6, 4,
             4, 2, 8, 3, 4, 4, 6, 2, 8, 2, 6, 4, 4, 4, 9, 2, 4, 4, 8, 2, 8, 2])

    def test_gcd(self) -> None:
        self.assertEqual(divs.gcd(2, 1), 1)
        self.assertEqual(divs.gcd(2, 3), 1)
        self.assertEqual(divs.gcd(2, 2), 2)
        self.assertEqual(divs.gcd(2, 4), 2)
        self.assertEqual(divs.gcd(20, 16), 4)
        self.assertEqual(divs.gcd(54, 24), 6)
        self.assertEqual(divs.gcd(45, 54), 9)
        self.assertEqual(divs.gcd(30, 105), 15)
        self.assertEqual(divs.gcd(452713601, 662853843), 3581)

    def test_is_coprime_pair(self) -> None:
        self.assertTrue(divs.is_coprime_pair(2, 1))
        self.assertTrue(divs.is_coprime_pair(3, 1))
        self.assertFalse(divs.is_coprime_pair(2, 2))
        self.assertTrue(divs.is_coprime_pair(2, 3))
        self.assertFalse(divs.is_coprime_pair(2, 4))
        self.assertFalse(divs.is_coprime_pair(45, 21))
        self.assertFalse(divs.is_coprime_pair(32, 58))
        self.assertTrue(divs.is_coprime_pair(70, 27))
        self.assertTrue(divs.is_coprime_pair(36, 77))
        self.assertTrue(divs.is_coprime_pair(41327, 75600))
        self.assertTrue(divs.is_coprime_pair(94753, 22416))
        self.assertFalse(divs.is_coprime_pair(94755, 22416))

    def test_lcm(self) -> None:
        self.assertEqual(divs.lcm(1, 1), 1)
        self.assertEqual(divs.lcm(1, 2), 2)
        self.assertEqual(divs.lcm(2, 1), 2)
        self.assertEqual(divs.lcm(2, 3), 6)
        self.assertEqual(divs.lcm(3, 2), 6)
        self.assertEqual(divs.lcm(2, 4), 4)
        self.assertEqual(divs.lcm(3, 4), 12)
        self.assertEqual(divs.lcm(6, 4), 12)
        self.assertEqual(divs.lcm(6, 21), 42)
        self.assertEqual(divs.lcm(18, 12), 36)
        self.assertEqual(divs.lcm(15, 35), 105)
        self.assertEqual(divs.lcm(55250154, 21071889), 20608307442)

    def test_lcm_all(self) -> None:
        self.assertEqual(divs.lcm_all([1]), 1)
        self.assertEqual(divs.lcm_all((1, 1)), 1)
        self.assertEqual(divs.lcm_all([1, 1, 1]), 1)
        self.assertEqual(divs.lcm_all({1, 2}), 2)
        self.assertEqual(divs.lcm_all([3, 4]), 12)
        self.assertEqual(divs.lcm_all((35, 15)), 105)
        self.assertEqual(divs.lcm_all([55250154, 21071889]), 20608307442)
        self.assertEqual(divs.lcm_all([2, 1, 1]), 2)
        self.assertEqual(divs.lcm_all(range(1, 4)), 6)
        self.assertEqual(divs.lcm_all({2, 64, 8}), 64)
        self.assertEqual(divs.lcm_all((8, 9, 7)), 504)
        self.assertEqual(divs.lcm_all([4, 7, 2, 5, 3]), 420)
        self.assertEqual(
            divs.lcm_all([540330, 424130, 465962, 357896]),
            4871660667720)
        
    def test_radical(self) -> None:
        rads = [1, 2, 3, 2, 5, 6, 7, 2, 3, 10, 11, 6, 13, 14, 15, 2, 17, 6, 19]
        for i, n in enumerate(rads):
            self.assertEqual(divs.radical(i + 1), n)
        self.assertEqual(divs.radical(1391500), 2530)
        self.assertEqual(divs.radical(21902926704), 73996374)
        
    def test_sum_divisors(self) -> None:
        div_sums = [1, 3, 4, 7, 6, 12, 8, 15, 13, 18, 12, 28, 14, 24, 24, 31]
        for i, n in enumerate(div_sums):
            self.assertEqual(divs.sum_divisors(i + 1), n)
        self.assertEqual(divs.sum_divisors(892), 1568)
        self.assertEqual(divs.sum_divisors(81468), 215488)
        self.assertEqual(divs.sum_divisors(1485436710), 3774758112)
        
    def test_sum_proper_divisors(self) -> None:
        div_sums = [0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10, 9, 15, 1, 21]
        for i, n in enumerate(div_sums):
            self.assertEqual(divs.sum_proper_divisors(i + 1), n)
        self.assertEqual(divs.sum_proper_divisors(900), 1921)
        self.assertEqual(divs.sum_proper_divisors(36582), 54810)
        self.assertEqual(divs.sum_proper_divisors(9145116791), 203174473)
        
    def test_totient(self) -> None:
        tots = [1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8]
        for i, n in enumerate(tots):
            self.assertEqual(divs.totient(i + 2), n)
        self.assertEqual(divs.totient(2, prime_factors=[2]), 1)
        self.assertEqual(divs.totient(3, prime_factors=[3]), 2)
        self.assertEqual(divs.totient(4, prime_factors=[2]), 2)
        self.assertEqual(divs.totient(5, prime_factors=[5]), 4)
        self.assertEqual(divs.totient(6, prime_factors=[2, 3]), 2)
        self.assertEqual(divs.totient(7, prime_factors=[7]), 6)
        self.assertEqual(divs.totient(68), 32)
        self.assertEqual(divs.totient(68, [2, 17]), 32)
        self.assertEqual(divs.totient(876, prime_factors=[2, 3, 73]), 288)
        self.assertEqual(divs.totient(876), 288)
        self.assertEqual(divs.totient(58758), 16776)
        self.assertEqual(
            divs.totient(58758, prime_factors=[2, 3, 7, 1399]),
            16776)
        self.assertEqual(
            divs.totient(19614162799, prime_factors=[7, 11, 31, 24097]),
            14790124800)
        self.assertEqual(divs.totient(19614162799), 14790124800)

    def test_totients_up_to(self) -> None:
        self.assertEqual(divs.totients_up_to(2), [1])
        self.assertEqual(divs.totients_up_to(3), [1, 2])
        self.assertEqual(divs.totients_up_to(4), [1, 2, 2])
        self.assertEqual(divs.totients_up_to(5), [1, 2, 2, 4])
        self.assertEqual(divs.totients_up_to(6), [1, 2, 2, 4, 2])
        self.assertEqual(divs.totients_up_to(7), [1, 2, 2, 4, 2, 6])
        self.assertEqual(
            divs.totients_up_to(38),
            [1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12,
             10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18])


if __name__ == '__main__':
    unittest.main()
