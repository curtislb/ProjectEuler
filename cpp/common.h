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

#include <map>
#include <vector>

using namespace std;

namespace common {

/* TYPEDEFS ******************************************************************/

    typedef unsigned long long Natural;

/* CLASSES *******************************************************************/

    /*** Counter ***/

    template <class T> class Counter {
        private:
            /* The current running counts for each item. */
            map<T, Natural> counts;

        public:
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

            /* Adds a single instance to the count for each item in items. */
            void add(vector<T> items);

            /* Returns the current count for item. */
            Natural count(T item);

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

    /* Adds a single instance to the count for each item in items. */
    template <class T> void Counter<T>::add(vector<T> items) {
        typedef typename vector<T>::iterator iterator;
        for (iterator i = items.begin(); i != items.end(); ++i)
            this->add(*i);
    }

    /* Returns the current count for item. */
    template <class T> Natural Counter<T>::count(T item) {
        if (counts.count(item))
            return counts[item];
        return 0;
    }

    /*
     * Merges the counts of this Counter with other. Items not counted
     * will be added to the counter. If an item has been counted, the
     * merge behavior is determined by rule.
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
