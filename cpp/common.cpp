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

/* STATIC *********************************************************************/

/* Currently computed terms of the Fibonacci sequence (in sorted order). */
static vector<unsigned long long> fibonacci_sequence (2, 1U);

/* Currently computed prime number terms (in sorted order). */
static vector<unsigned long long> prime_sequence (1, 2U);

/* Precomputes and stores the first n Fibonacci numbers. */
static void computeFibonacci(unsigned int n) {
    unsigned int fib_count = fibonacci_sequence.size();

    // have the first n numbers already been computed?
    if (n < fib_count)
        return;

    // make room for numbers to be added to sequence
    fibonacci_sequence.reserve(n - fib_count + 1);

    // compute numbers iteratively from existing sequence
    unsigned long long f0 = fibonacci_sequence[fib_count - 2];
    unsigned long long f1 = fibonacci_sequence[fib_count - 1];
    unsigned long long temp;
    for (unsigned int count = fib_count; count <= n; count++) {
        temp = f1;
        f1 += f0;
        f0 = temp;
        fibonacci_sequence.push_back(f1);
    }
}

/* Precomputes and stores the Fibonacci numbers up to at least f. */
static void computeFibonacciUpTo(unsigned long long f) {
    unsigned int fib_count = fibonacci_sequence.size();

    // have the numbers up to f already been computed?
    if (fibonacci_sequence[fib_count - 1] >= f)
        return;

    // compute numbers iteratively from existing sequence
    unsigned long long f0 = fibonacci_sequence[fib_count - 2];
    unsigned long long f1 = fibonacci_sequence[fib_count - 1];
    unsigned long long temp;
    while (f1 < f) {
        temp = f1;
        f1 += f0;
        f0 = temp;
        fibonacci_sequence.push_back(f1);
    }
}

/* Precomputes and stores the first n prime numbers. */
static void computePrimes(unsigned int n) {
    unsigned int prime_count = prime_sequence.size();

    // have the first n primes already been computed?
    if (n < prime_count)
        return;

    // TODO ...
}

/* Precomputes and stores the prime numbers up to p. */
static void computePrimesUpTo(unsigned long long p) {
    unsigned int prime_count = prime_sequence.size();

    // have the numbers up to p already been computed?
    unsigned long long prime_max = prime_sequence[prime_count - 1];
    if (prime_max >= p)
        return;

    // prepare sieve of Eratosthenes for numbers (prime_max + 1) to p
    unsigned int sieve_size = p - prime_max;
    vector<bool> sieve (sieve_size, true);

    // sift out composite numbers using previously computed primes
    unsigned long long rho;
    for (unsigned int i = 0U; i < prime_count; i++) {
        rho = prime_sequence[i];
        for (unsigned long long j = rho * rho; j < sieve_size + prime_max + 1; j += rho) {
            if (j < prime_max + 1)
                continue;
            sieve[j - prime_max - 1] = false;
        }
    }

    // sift out remaining composite numbers with newly found primes
    for (unsigned int i = 0U; i < sieve_size; i++) {
        if (sieve[i]) {
            rho = i + prime_max + 1;
            prime_sequence.push_back(rho);
            for (unsigned long long j = rho * rho - prime_max - 1; j < sieve_size; j += rho)
                sieve[j] = false;
        }
    }
}

/* COMMON *********************************************************************/

namespace common {
    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long arithSeries(long a, long n, long d) {
        return n * (2 * a + (n - 1) * d) / 2;
    }

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    unsigned long long fibonacci(unsigned int n) {
        computeFibonacci(n);
        return fibonacci_sequence[n];
    }

    /* Returns the first n Fibonacci numbers. */
    vector<unsigned long long> fibonacciNums(unsigned int n) {
        computeFibonacci(n);
        vector<unsigned long long> f_list (fibonacci_sequence.begin(), fibonacci_sequence.begin() + n);
        return f_list;
    }

    /* Returns the Fibonacci numbers up to f. */
    vector<unsigned long long> fibonacciNumsUpTo(unsigned long long f) {
        computeFibonacciUpTo(f);
        unsigned int i = 0U;
        while (fibonacci_sequence[i] <= f)
            i++;
        vector<unsigned long long> f_list (fibonacci_sequence.begin(), fibonacci_sequence.begin() + i);
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
        for (unsigned int i = 5U; i < (unsigned int)ceil(sqrt((long double)n)); i += 6) {
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
        long long half_pow = power(m, n / 2);

        // compute original power
        if (n % 2 == 0)
            return half_pow * half_pow;
        else
            return m * half_pow * half_pow;
    }

    /* Returns the nth prime number. */
    unsigned long long prime(unsigned int n) {
        computePrimes(n);
        return prime_sequence[n];
    }

    /* Returns the first n prime numbers. */
    vector<unsigned long long> primes(unsigned int n) {
        computePrimes(n);
        vector<unsigned long long> p_list (prime_sequence.begin(), prime_sequence.begin() + n);
        return p_list;
    }

    /* Returns the prime numbers up to p. */
    vector<unsigned long long> primesUpTo(unsigned long long p) {
        computePrimesUpTo(p);
        unsigned int i = 0U;
        while (i < prime_sequence.size() && prime_sequence[i] <= p)
            i++;
        vector<unsigned long long> p_list (prime_sequence.begin(), prime_sequence.begin() + i);
        return p_list;
    }
}
