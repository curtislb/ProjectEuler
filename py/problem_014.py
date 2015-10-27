"""problem_014.py

Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under LIMIT, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above LIMIT.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 1000000 # default: 1000000

# SOLUTION ####################################################################

@com.memoized
def collatz_length(n):
    """Returns the number of terms in the Collatz sequence starting from n."""
    if n == 1:
        return 1
    return 1 + collatz_length(com.collatz_step(n))


def main_thread():
    # search for longest Collatz sequence starting below LIMIT
    global best_num
    best_num = 0
    best_length = 0
    for i in range(2, LIMIT):
        length = collatz_length(i)
        if length > best_length:
            best_num = i
            best_length = length


def main():
    com.run_thread(main_thread)
    return best_num


if __name__ == '__main__':
    print(main())
