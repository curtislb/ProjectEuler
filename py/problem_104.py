'''
Problem 104.

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n - 1) + F(n - 2), where F(1) = 1 and F(2) = 1.
It turns out that F(541), which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F(2749), which contains 575
digits, is the first Fibonacci number for which the first nine digits are 1-9
pandigital.

Given that F(k) is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.

@author: Curtis Belmonte
'''
from common import big_mod, fibonacci, is_permutation, PAN_STR, run_thread

def main():
    lo_div = 10**9
    
    def test_104(fib_num):
        if is_permutation(str(big_mod(fib_num, lo_div)), PAN_STR):
            return is_permutation(str(fib_num)[:9], PAN_STR)
    
    k = 2750
    fib_num = fibonacci(k)
    while not test_104(fib_num):
        k += 1
        fib_num = fibonacci(k)
    print(k + 1)
    
run_thread(main)