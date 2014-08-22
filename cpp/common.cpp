/*
 * common.cpp
 *
 * Common utility functions for various Project Euler problems.
 *
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#include <iostream>
#include <sstream>
#include <vector>

#include <math.h>

#include "common.h"

using namespace std;

/* TYPEDEFS ******************************************************************/

typedef unsigned long long fibonacci_t;
typedef unsigned long long prime_t;

/* STATIC ********************************************************************/

/* Currently computed terms of the Fibonacci sequence (in sorted order). */
static vector<fibonacci_t> fibonacci_sequence (2, 1);

/* Currently computed prime number terms (in sorted order). */
static vector<prime_t> prime_sequence (1, 2);

/* Precomputes and stores the first n Fibonacci numbers. */
static void computeFibonacci(unsigned int n) {
    const unsigned int kFibCount = fibonacci_sequence.size();

    // have the first n numbers already been computed?
    if (n < kFibCount)
        return;

    // make room for numbers to be added to sequence
    fibonacci_sequence.reserve(n - kFibCount + 1);

    // compute numbers iteratively from existing sequence
    fibonacci_t f0 = fibonacci_sequence[kFibCount - 2];
    fibonacci_t f1 = fibonacci_sequence[kFibCount - 1];
    fibonacci_t temp;
    for (unsigned int count = kFibCount; count <= n; count++) {
        temp = f1;
        f1 += f0;
        f0 = temp;
        fibonacci_sequence.push_back(f1);
    }
}

/* Precomputes and stores the Fibonacci numbers up to at least f. */
static void computeFibonacciUpTo(fibonacci_t f) {
    const unsigned int kFibCount = fibonacci_sequence.size();

    // have the numbers up to f already been computed?
    if (fibonacci_sequence[kFibCount - 1] >= f)
        return;

    // compute numbers iteratively from existing sequence
    fibonacci_t f0 = fibonacci_sequence[kFibCount - 2];
    fibonacci_t f1 = fibonacci_sequence[kFibCount - 1];
    fibonacci_t temp;
    while (f1 < f) {
        temp = f1;
        f1 += f0;
        f0 = temp;
        fibonacci_sequence.push_back(f1);
    }
}

/* Precomputes and stores the first n prime numbers. */
static void computePrimes(unsigned int n) {
    unsigned int kPrimeCount = prime_sequence.size();

    // have the first n primes already been computed?
    if (n < kPrimeCount)
        return;

    // TODO ...
}

/* Precomputes and stores the prime numbers up to p. */
static void computePrimesUpTo(prime_t p) {
    const unsigned int kPrimeCount = prime_sequence.size();

    // have the numbers up to p already been computed?
    prime_t prime_max = prime_sequence[kPrimeCount - 1];
    if (prime_max >= p)
        return;

    // prepare sieve of Eratosthenes for numbers prime_max+1 to p
    const unsigned int kSieveSize = p - prime_max;
    vector<bool> sieve (kSieveSize, true);

    // sift out composite numbers using previously computed primes
    prime_t rho;
    for (unsigned int i = 0; i < kPrimeCount; i++) {
        rho = prime_sequence[i];
        for (prime_t j = rho * rho; j < kSieveSize + prime_max + 1; j += rho) {
            if (j < prime_max + 1)
                continue;
            sieve[j - prime_max - 1] = false;
        }
    }

    // sift out remaining composite numbers with newly found primes
    for (unsigned int i = 0; i < kSieveSize; i++) {
        if (sieve[i]) {
            rho = i + prime_max + 1;
            prime_sequence.push_back(rho);
            for (prime_t j = rho * rho - prime_max - 1; j < kSieveSize; j += rho)
                sieve[j] = false;
        }
    }
}

/* COMMON ********************************************************************/

namespace common {
    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long arithSeries(long a, long n, long d) {
        return n * (2 * a + (n - 1) * d) / 2;
    }

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    fibonacci_t fibonacci(unsigned int n) {
        computeFibonacci(n);
        return fibonacci_sequence[n];
    }

    /* Returns the first n Fibonacci numbers. */
    vector<fibonacci_t> fibonacciNums(unsigned int n) {
        computeFibonacci(n);

        vector<fibonacci_t> f_list (fibonacci_sequence.begin(), fibonacci_sequence.begin() + n);
        return f_list;
    }

    /* Returns the Fibonacci numbers up to f. */
    vector<unsigned long long> fibonacciNumsUpTo(fibonacci_t f) {
        computeFibonacciUpTo(f);

        unsigned int i = 0;
        const unsigned int kFibCount = fibonacci_sequence.size();
        while (i < kFibCount && fibonacci_sequence[i] <= f)
            i++;

        vector<fibonacci_t> f_list (fibonacci_sequence.begin(), fibonacci_sequence.begin() + i);
        return f_list;
    }

    /* Returns the greatest common divisor of m and n. */
    int gcd(int m, int n) {
        // find gcd using Euler's method
        int temp;
        while (n != 0) {
            temp = n;
            n = m % n;
            m = temp;
        }
        return m;
    }

    /* Determines if the natural number n is a palindrome. */
    bool isPalindrome(unsigned long long n) {
        // convert n to a string
        ostringstream n_stringstream;
        n_stringstream << n;
        string n_string = n_stringstream.str();

        // compare chars iteratively from beginning and end of string
        int i = 0;
        int j = n_string.length() - 1;
        while (i < j) {
            if (n_string[i] != n_string[j])
                return false;
            i++;
            j--;
        }
        return true;
    }

    /* Determines if the natural number n is prime. */
    bool isPrime(unsigned int n) {
        // base cases for small n
        if (n <= 3) {
            if (n <= 1)
                return false;
            return true;
        }

        // check if multiple of 2 or 3
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        // search for subsequent factors in increments of 6
        const unsigned int kMaxFactor = ceil(sqrt(n));
        for (unsigned int i = 5; i < kMaxFactor; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    /* Returns the least common multiple of m and n. */
    int lcm(int m, int n) {
        return m * n / gcd(m, n);
    }

    /* Returns the value of m raised to the n power. */
    long long power(long m, unsigned int n) {
        // base case: m^0 = 1
        if (n == 0)
            return 1;

        // recursively compute half power
        const long long kHalfPow = power(m, n / 2);

        // compute original power
        if (n % 2 == 0)
            return kHalfPow * kHalfPow;
        else
            return m * kHalfPow * kHalfPow;
    }

    /* Returns the nth prime number. */
    unsigned long long prime(unsigned int n) {
        computePrimes(n);
        return prime_sequence[n];
    }

    /* Returns the first n prime numbers. */
    vector<unsigned long long> primes(unsigned int n) {
        computePrimes(n);

        vector<prime_t> p_list (prime_sequence.begin(), prime_sequence.begin() + n);
        return p_list;
    }

    /* Returns the prime numbers up to p. */
    vector<unsigned long long> primesUpTo(prime_t p) {
        computePrimesUpTo(p);

        unsigned int i = 0;
        const unsigned int kPrimeCount = prime_sequence.size();
        while (i < kPrimeCount && prime_sequence[i] <= p)
            i++;

        vector<prime_t> p_list (prime_sequence.begin(), prime_sequence.begin() + i);
        return p_list;
    }
}
