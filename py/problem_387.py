#!/usr/bin/env python3

"""problem_387.py

Problem 387: Harshad Numbers

A Harshad or Niven number is a number that is divisible by the sum of its
digits. 201 is a Harshad number because it is divisible by 3 (the sum of its
digits.)

When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad
number. Let's call a Harshad number that, while recursively truncating the last
digit, always results in a Harshad number a right truncatable Harshad number.

Also: 201 / 3 = 67 which is prime. Let's call a Harshad number that, when
divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime. When we truncate the last digit from
it we get 201, a strong Harshad number that is also right truncatable. Let's
call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less
than 10^4 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^POWER.
"""

__author__ = 'Curtis Belmonte'

import common.primes as prime


# PARAMETERS ##################################################################


POWER = 14 # default: 14


# SOLUTION ####################################################################


def solve() -> int:
    total = 0

    # search for strong RTH primes with each number of digits up to POWER - 1
    rth_num_sums = [(0, 0)]
    for _ in range(POWER - 1):
        # build new RTH numbers by adding digits to previous list
        new_rth_num_sums = []
        candidate_nums = []
        for base_num, base_sum in rth_num_sums:
            base_part = base_num * 10
            for digit in range(10):
                new_num = base_part + digit
                new_sum = base_sum + digit

                # avoid dividing by 0
                if new_sum == 0:
                    continue

                # keep track of all strong RTH numbers
                div, mod = divmod(new_num, new_sum)
                if mod == 0:
                    new_rth_num_sums.append((new_num, new_sum))
                    if prime.is_prime(div):
                        candidate_nums.append(new_num)

        # prepare RTH numbers and their digit sums for next iteration
        rth_num_sums = new_rth_num_sums

        # check for strong RTH primes formed from RTH number bases
        for base_num in candidate_nums:
            base_part = base_num * 10
            for digit in range(1, 10, 2):
                n = base_part + digit
                if prime.is_prime(n):
                    total += n

    return total


if __name__ == '__main__':
    print(solve())
