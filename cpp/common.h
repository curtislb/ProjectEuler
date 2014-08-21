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

namespace common {
    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long arithSeries(long a, long n, long d);

    /* Precomputes and stores the first n Fibonacci numbers. */
    void computeFibonacci(unsigned int n);

    /* Precomputes and stores the Fibonacci numbers up to at least f. */
    void computeFibonacciUpTo(unsigned long long f);

    /* Precomputes and stores the prime numbers up to p. */
    void computePrimesUpTo(unsigned long long p);

    /* Returns the n'th Fibonacci number, with F(0) = F(1) = 1. */
    unsigned long long fibonacci(unsigned int n);

    /* Returns the greatest common divisor of m and n */
    int gcd(int m, int n);

    /* Determines if the natural number n is prime. */
    bool isPrime(unsigned int n);

    /* Returns the least common multiple of m and n. */
    int lcm(int m, int n);

    unsigned long long prime(unsigned int n);
}

#endif /* COMMON_H_ */
