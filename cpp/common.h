/*
 * common.h
 *
 * Common utility functions and classes for various Project Euler problems.
 *
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#ifndef COMMON_H_
#define COMMON_H_

#include <map>
#include <vector>

using namespace std;

namespace common {

/* TYPEDEFS ******************************************************************/

    typedef unsigned long long Natural;

/* CLASSES *******************************************************************/

    /*** BigInteger ***/

    /* Represents an nonnegative integer number of arbitrary length. */
    class BigInteger {
        private:
            /* The digits in the decimal representation of the integer. */
            vector<short> digits;

        public:
            /* Constructs a new BigInteger. */
            BigInteger();

            /*
             * Constructs a BigInteger from its numerical representation as a
             * decimal integer in the C-style string int_string.
             */
            BigInteger(const char *int_string);

            /* Constructs a BigInteger from the natural number n. */
            BigInteger(Natural n);

            /*
             * Constructs a BigInteger from its numerical representation as a
             * decimal integer in the string int_string.
             */
            BigInteger(const string int_string);

            /* Returns the sum of this BigInteger and other. */
            BigInteger operator+(const BigInteger &other);

            /* Adds the value of other to this BigInteger. */
            BigInteger &operator+=(const BigInteger &other);

            /* Returns the difference of this BigInteger and other. */
            BigInteger operator-(const BigInteger &other);

            /* Subtracts the value of other from this BigInteger. */
            BigInteger &operator-=(const BigInteger &other);

            /* Returns the product of this BigInteger and other. */
            BigInteger operator*(const BigInteger &other);

            /* Multiplies this BigInteger by the value of other. */
            BigInteger &operator*=(const BigInteger &other);

            /* Returns the decimal string representation of this BigInteger. */
            string asString();
    };

    /*** Counter ***/

    /* Counts the number of occurrences of individual items. */
    template <class T> class Counter {
        private:
            /* The current running counts for each item. */
            map<T, Natural> counts;

        public:
            /* Iterator type for the Counter class. */
            typedef typename map<T, Natural>::iterator iterator;

            /* Rules for handling conflicts when merging Counter objects. */
            enum MergeRule {
                MERGE_FAVOR_THIS,  // favor the current count
                MERGE_FAVOR_OTHER, // favor the other count
                MERGE_FAVOR_HIGH,  // favor the higher count
                MERGE_FAVOR_LOW,   // favor the lower count
                MERGE_SUM_COUNTS   // sum the counts
            };

            /* Adds a single instance of item to the running count. */
            void add(T item);

            /* Adds n instances of item to the running count. */
            void add(T item, Natural n);

            /* Adds a single instance to the count for each item in items. */
            void add(vector<T> items);

            /* Returns an iterator pointing to the beginning of the Counter. */
            iterator begin();

            /* Returns the current count for item. */
            Natural count(T item);

            /* Returns an iterator pointing to the end of the Counter. */
            iterator end();

            /*
             * Merges the counts of this Counter with other. Items not counted
             * will be added to the counter. If an item has been counted, the
             * merge behavior is determined by rule.
             */
            void merge(Counter<T> *other, MergeRule rule);
    };

    /* Adds a single instance of item to the running count. */
    template <class T> void Counter<T>::add(T item) {
        if (counts.count(item))
            counts[item]++;
        else
            counts[item] = 1;
    }

    /* Adds a single instance of item to the running count. */
    template <class T> void Counter<T>::add(T item, Natural n) {
        counts[item] += n;
    }

    /* Adds a single instance to the count for each item in items. */
    template <class T> void Counter<T>::add(vector<T> items) {
        typedef typename vector<T>::iterator iterator;
        for (iterator i = items.begin(); i != items.end(); ++i)
            this->add(*i);
    }

    /* Returns an iterator pointing to the beginning of the Counter. */
    template <class T> typename Counter<T>::iterator Counter<T>::begin() {
        return counts.begin();
    }

    /* Returns the current count for item. */
    template <class T> Natural Counter<T>::count(T item) {
        if (counts.count(item))
            return counts[item];
        return 0;
    }

    /* Returns an iterator pointing to the end of the Counter. */
    template <class T> typename Counter<T>::iterator Counter<T>::end() {
        return counts.end();
    }

    /*
     * Merges the counts of this Counter with other. Items not counted will be
     * added to the counter. If an item has been counted, the merge behavior is
     * determined by rule.
     */
    template <class T> void Counter<T>::merge(Counter *other, MergeRule rule) {
        // merge each item count from other Counter
        T item;
        Natural item_count;
        typedef typename map<T, Natural>::iterator iterator;
        for (iterator i = other->counts.begin(); i != other->counts.end(); ++i) {
            item = i->first;
            item_count = i->second;

            if (!counts.count(item)) {
                // add the new item count to this Counter
                counts[item] = item_count;
            } else {
                switch (rule) {
                    // favor the current count
                    case MERGE_FAVOR_THIS:
                        break;

                    // favor the other count
                    case MERGE_FAVOR_OTHER:
                        counts[item] = item_count;
                        break;

                    // favor the higher count
                    case MERGE_FAVOR_HIGH:
                        counts[item] = max(counts[item], item_count);
                        break;

                    // favor the lower count
                    case MERGE_FAVOR_LOW:
                        counts[item] = min(counts[item], item_count);
                        break;

                    // sum the counts
                    case MERGE_SUM_COUNTS:
                        counts[item] += item_count;
                        break;
                }
            }
        }
    }

/* FUNCTIONS *****************************************************************/

    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long long arithSeries(long long a, long long n, long long d);

    /* Returns the numeric value of character c, representing a digit 0-9.  */
    short charToDigit(char c);

    /* Returns the next number in the Collatz sequence following n. */
    Natural collatzStep(Natural n);

    /* Returns the number of digits of the natural number n. */
    unsigned int countDigits(Natural n);

    /* Returns the number of divisors of the natural number n. */
    unsigned int countDivisors(Natural n);

    /* Returns the natural number represented by the digit vector digits. */
    Natural digitsToNumber(const vector<short> digits);

    /* Returns the factorial of n, defined as n! = n * (n - 1) * ... * 1. */
    Natural factorial(unsigned int n);

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

    /* Returns a matrix of integer numbers read from input_file. */
    vector<vector<long> > matrixFromFile(const char *input_file);

    /* Returns a vector of the digits of the natural number n. */
    vector<short> numberToDigits(Natural n);

    /* Returns the number of permutations of k objects from a group of n. */
    Natural permutations(Natural n, Natural k);

    /* Returns the value of m raised to the nth power. */
    Natural power(Natural m, unsigned int n);

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

    /* Returns the sum of the squares of the first n natural numbers. */
    Natural sumOfSquares(unsigned int n);

    /*
     * Returns the nth triangle number, or the sum of the natural numbers up to
     * and including n.
     */
    Natural triangle(unsigned int n);
}

#endif /* COMMON_H_ */
