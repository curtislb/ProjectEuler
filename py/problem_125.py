"""problem_125.py

Problem 125: 

The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164.

NOTE: 1 = 0^2 + 1^2 has not been included as this problem is concerned with
the squares of positive integers.

Find the sum of all the numbers less than N that are both palindromic and can
be written as the sum of consecutive squares.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

N = 10**8 # default: 10**8

# SOLUTION ####################################################################

def solve():
    # find max value for which sum of squares is less than N
    k_max = 2
    while com.sum_of_squares(k_max) < N:
        k_max += 1

    # construct sums of squares and check for palindromes
    palindromes = set()
    for k in range(2, k_max):
        n = k
        sum_to_k = com.triangle_number(k - 1)
        sum_squares_to_k = com.sum_of_squares(k - 1)
        while True:
            square_sum = (k * n**2) - (2 * n * sum_to_k) + sum_squares_to_k
            
            # break and advance k once square sum reaches N
            if square_sum >= N:
                break
            
            if com.is_palindrome(square_sum):
                palindromes.add(square_sum)
            
            n += 1

    # return sum of deduplicated plaindromes
    return sum(palindromes)


if __name__ == '__main__':
    print(solve())
