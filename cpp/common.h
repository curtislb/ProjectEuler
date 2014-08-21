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
    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long arithSeries(long a, long n, long d);

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    unsigned long long fibonacci(unsigned int n);

    /* Returns the first n Fibonacci numbers. */
    vector<unsigned long long> fibonacciNums(unsigned int n);

    /* Returns the Fibonacci numbers up to f. */
    vector<unsigned long long> fibonacciNumsUpTo(unsigned long long f);

    /* Returns the greatest common divisor of m and n. */
    int gcd(int m, int n);

    /* Determines if the natural number n is a palindrome. */
    bool isPalindrome(unsigned long long n);

    /* Determines if the natural number n is prime. */
    bool isPrime(unsigned int n);

    /* Returns the least common multiple of m and n. */
    int lcm(int m, int n);

    /* Returns the value of m raised to the n power. */
    long long power(long m, unsigned int n);

    /* Returns the nth prime number. */
    unsigned long long prime(unsigned int n);

    /* Returns the first n prime numbers. */
    vector<unsigned long long> primes(unsigned int n);

    /* Returns the prime numbers up to p. */
    vector<unsigned long long> primesUpTo(unsigned long long p);
}

#endif /* COMMON_H_ */
