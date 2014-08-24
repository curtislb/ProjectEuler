/*
 * common.cpp
 *
 * Common utility functions and classes for various Project Euler problems.
 *
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#include <iostream>
#include <map>
#include <sstream>
#include <utility>
#include <vector>

#include <math.h>

#include "common.h"

using namespace std;

namespace common {

/* STATIC VARIABLES **********************************************************/

    /* Currently computed terms of the Fibonacci sequence (in sorted order). */
    static vector<Natural> fibonacci_sequence(2, 1);

    /* Currently computed prime number terms (in sorted order). */
    static vector<Natural> prime_sequence(1, 2);

/* STATIC FUNCTIONS **********************************************************/

    /*** Declarations ***/

    /* Precomputes and stores the first n Fibonacci numbers. */
    static void computeFibonacci(unsigned int n);

    /* Precomputes and stores the Fibonacci numbers up to at least n. */
    static void computeFibonacciUpTo(Natural n);

    /* Precomputes and stores the first n prime numbers. */
    static void computePrimes(unsigned int n);

    /* Precomputes and stores the prime numbers up to n. */
    static void computePrimesUpTo(Natural n);

    /*** Implementations ***/

    /* Precomputes and stores the first n Fibonacci numbers. */
    static void computeFibonacci(unsigned int n) {
        const unsigned int kFibCount = fibonacci_sequence.size();

        // have the first n numbers already been computed?
        if (n < kFibCount)
            return;

        // make room for numbers to be added to sequence
        fibonacci_sequence.reserve(n - kFibCount + 1);

        // compute numbers iteratively from existing sequence
        Natural f0 = fibonacci_sequence[kFibCount - 2];
        Natural f1 = fibonacci_sequence[kFibCount - 1];
        Natural temp;
        for (unsigned int count = kFibCount; count <= n; count++) {
            temp = f1;
            f1 += f0;
            f0 = temp;
            fibonacci_sequence.push_back(f1);
        }
    }

    /* Precomputes and stores the Fibonacci numbers up to at least n. */
    static void computeFibonacciUpTo(Natural n) {
        const unsigned int kFibCount = fibonacci_sequence.size();

        // have the numbers up to f already been computed?
        if (fibonacci_sequence[kFibCount - 1] >= n)
            return;

        // compute numbers iteratively from existing sequence
        Natural f0 = fibonacci_sequence[kFibCount - 2];
        Natural f1 = fibonacci_sequence[kFibCount - 1];
        Natural temp;
        while (f1 < n) {
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

        // TODO: implement incremental sieve?

        // based on analysis of OEIS data set A006880 and empirical time tests
        const Natural kEstimate = n <= 25 ? 100 : n * log(n) * 1.05 + n * 0.87;
        const Natural kIncrement = n / log(n);

        // compute primes up to estimate, then step forward until n are found
        for (Natural i = kEstimate; prime_sequence.size() < n; i += kIncrement)
            computePrimesUpTo(i);
    }

    /* Precomputes and stores the prime numbers up to n. */
    static void computePrimesUpTo(Natural n) {
        const unsigned int kPrimeCount = prime_sequence.size();

        // have the numbers up to p already been computed?
        Natural prime_max = prime_sequence[kPrimeCount - 1];
        if (prime_max >= n)
            return;

        // prepare sieve of Eratosthenes for numbers prime_max+1 to p
        const unsigned int kSieveSize = n - prime_max;
        vector<bool> sieve(kSieveSize, true);

        // sift out composite numbers using previously computed primes
        Natural rho;
        for (unsigned int i = 0; i < kPrimeCount; i++) {
            rho = prime_sequence[i];
            for (Natural j = rho*rho; j < kSieveSize + prime_max + 1; j += rho) {
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
                for (Natural j = rho*rho - prime_max - 1; j < kSieveSize; j += rho)
                    sieve[j] = false;
            }
        }
    }

/* FUNCTIONS *****************************************************************/

    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long long arithSeries(long long a, long long n, long long d) {
        return n * (2 * a + (n - 1) * d) / 2;
    }

    /* Returns the numeric value of character c, representing a digit 0-9.  */
    int charToDigit(char c) {
        return c - '0';
    }

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    Natural fibonacci(unsigned int n) {
        computeFibonacci(n);
        return fibonacci_sequence[n];
    }

    /* Returns the first n Fibonacci numbers. */
    vector<Natural> fibonacciNums(unsigned int n) {
        computeFibonacci(n);

        vector<Natural> f_list(fibonacci_sequence.begin(), fibonacci_sequence.begin() + n);
        return f_list;
    }

    /* Returns the Fibonacci numbers up to n. */
    vector<Natural> fibonacciNumsUpTo(Natural n) {
        computeFibonacciUpTo(n);

        unsigned int i = 0;
        const unsigned int kFibCount = fibonacci_sequence.size();
        while (i < kFibCount && fibonacci_sequence[i] <= n)
            i++;

        vector<Natural> f_list(fibonacci_sequence.begin(), fibonacci_sequence.begin() + i);
        return f_list;
    }

    /* Returns the greatest common divisor of m and n. */
    Natural gcd(Natural m, Natural n) {
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
    bool isPalindrome(Natural n) {
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
    bool isPrime(Natural n) {
        // base cases for small n
        if (n <= 3) {
            if (n <= 1)
                return false;
            return true;
        }

        // check if multiple of 2 or 3
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        // search for subsequent prime factors around multiples of 6
        const unsigned int kMaxFactor = sqrt(n);
        for (unsigned int i = 5; i <= kMaxFactor; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    /* Returns the least common multiple of m and n. */
    Natural lcm(Natural m, Natural n) {
        return m * n / gcd(m, n);
    }

    /* Returns the least common multiple of all numbers in nums. */
    Natural lcm(vector<Natural> nums) {
        Counter<Natural> *powers;
        Counter<Natural> *max_powers = new Counter<Natural>;
        vector<pair<Natural, unsigned int> > factors;
        for (vector<Natural>::iterator i = nums.begin(); i != nums.end(); ++i) {
            // compute powers of unique prime factors of the current num
            powers = new Counter<Natural>;
            factors = primeFactorization(*i);
            for (vector<pair<Natural, unsigned int> >::iterator j = factors.begin(); j != factors.end(); ++j)
                powers->add(j->first, j->second);

            // merge with current highest powers of unique prime factors
            max_powers->merge(powers, Counter<Natural>::MERGE_FAVOR_HIGH);
            delete powers;
        }

        // return the product of prime factors raised to their highest powers
        Natural product = 1;
        for (Counter<Natural>::iterator i = max_powers->begin(); i != max_powers->end(); ++i)
            product *= power(i->first, i->second);
        delete max_powers;
        return product;
    }

    /* Returns the value of m raised to the n power. */
    Natural power(Natural m, unsigned int n) {
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
    Natural prime(unsigned int n) {
        computePrimes(n);
        return prime_sequence[n - 1];
    }

    /*
     * Computes the prime factorization of the natural number n. Returns a
     * vector of base-exponent pairs containing each prime factor and its power
     * in the prime factorization.
     */
    vector<pair<Natural, unsigned int> > primeFactorization(Natural n) {
        // compute potential prime factors of n
        const vector<Natural> kPrimes = primesUpTo(n);
        const unsigned int kPrimeCount = kPrimes.size();

        pair<Natural, unsigned int> factor;
        vector<pair<Natural, unsigned int> > factorization;
        for (unsigned int i = 0; i < kPrimeCount; i++) {
            // has n already been completely factored?
            if (n == 1)
                break;

            // compute power of ith prime in factorization
            factor = make_pair(kPrimes[i], 0);
            while (n % kPrimes[i] == 0) {
                n /= kPrimes[i];
                factor.second++;
            }

            // add factor to factorization if necessary
            if (factor.second > 0)
                factorization.push_back(factor);
        }

        return factorization;
    }

    /* Returns the first n prime numbers. */
    vector<Natural> primes(unsigned int n) {
        computePrimes(n);

        vector<Natural> p_list(prime_sequence.begin(), prime_sequence.begin() + n);
        return p_list;
    }

    /* Returns the prime numbers up to p. */
    vector<Natural> primesUpTo(Natural p) {
        computePrimesUpTo(p);

        unsigned int i = 0;
        const unsigned int kPrimeCount = prime_sequence.size();
        while (i < kPrimeCount && prime_sequence[i] <= p)
            i++;

        vector<Natural> p_list(prime_sequence.begin(), prime_sequence.begin() + i);
        return p_list;
    }

    /* Returns the sum of the squares of the first n natural numbers. */
    Natural sumOfSquares(unsigned int n) {
        const Natural m = n;
        return (2 * m*m*m + 3 * m*m + m) / 6;
    }

    /*
     * Returns the nth triangle number, or the sum of the natural numbers up to
     * and including n.
     */
    Natural triangle(unsigned int n) {
        Natural m = n;
        return m * (m + 1) / 2;
    }
}
