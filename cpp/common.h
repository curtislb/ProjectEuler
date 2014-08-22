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
    long long arithSeries(long long a, long long n, long long d);

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    Natural fibonacci(unsigned int n);

    /* Returns the first n Fibonacci numbers. */
    vector<Natural> fibonacciNums(unsigned int n);

    /* Returns the Fibonacci numbers up to n. */
    vector<Natural> fibonacciNumsUpTo(Natural n);

    /* Returns the greatest common divisor of m and n. */
    Natural gcd(Natural m, Natural n);

    /* Determines if the natural number n is a palindrome. */
    bool isPalindrome(Natural n);

    /* Determines if the natural number n is prime. */
    bool isPrime(Natural n);

    /* Returns the least common multiple of m and n. */
    Natural lcm(Natural m, Natural n);

    /* Returns the least common multiple of all numbers in nums. */
    Natural lcm(vector<Natural> nums);

    /* Returns the value of m raised to the n power. */
    long long power(long long m, unsigned int n);

    /* Returns the nth prime number. */
    Natural prime(unsigned int n);

    /*
     * Computes the prime factorization of the natural number n. Returns a
     * vector of base-exponent pairs containing each prime factor and its power
     * in the prime factorization.
     */
    vector<pair<Natural, unsigned int> > primeFactorization(Natural n);

    /* Returns the first n prime numbers. */
    vector<Natural> primes(unsigned int n);

    /* Returns the prime numbers up to n. */
    vector<Natural> primesUpTo(Natural n);
}

#endif /* COMMON_H_ */
