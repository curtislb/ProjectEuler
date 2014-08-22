/*
 * common.h
 *
 * Common utility functions for various Project Euler problems.
 *
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#ifndef COMMON_H_
#define COMMON_H_

#include <vector>

using namespace std;

namespace common {

/* TYPEDEFS ******************************************************************/

    typedef unsigned long long Natural;

/* FUNCTIONS *****************************************************************/

    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long arithSeries(long a, long n, long d);

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    Natural fibonacci(unsigned int n);

    /* Returns the first n Fibonacci numbers. */
    vector<Natural> fibonacciNums(unsigned int n);

    /* Returns the Fibonacci numbers up to f. */
    vector<Natural> fibonacciNumsUpTo(Natural f);

    /* Returns the greatest common divisor of m and n. */
    int gcd(int m, int n);

    /* Determines if the natural number n is a palindrome. */
    bool isPalindrome(Natural n);

    /* Determines if the natural number n is prime. */
    bool isPrime(unsigned int n);

    /* Returns the least common multiple of m and n. */
    int lcm(int m, int n);



    /* Returns the value of m raised to the n power. */
    long long power(long m, unsigned int n);

    /* Returns the nth prime number. */
    Natural prime(unsigned int n);

    /* Returns the first n prime numbers. */
    vector<Natural> primes(unsigned int n);

    /* Returns the prime numbers up to p. */
    vector<Natural> primesUpTo(Natural p);
}

#endif /* COMMON_H_ */
