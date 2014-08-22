/*
 * problem004.cpp
 * 
 * Problem 4: Largest palindrome product
 *
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two D-digit numbers.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 21, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned int D = 3; // default: 3

/* SOLUTION ******************************************************************/

int main() {
    // calculate max and min D-digit numbers
    const long long kMinFactor = common::power(10, D - 1);
    const long long kMaxFactor = common::power(10, D) - 1;

    // multiply D-digit products to find largest palindrome
    long long product;
    long long best_answer = -1;
    for (long long i = kMaxFactor; i >= kMinFactor; i--) {
        for (long long j = i; j >= kMinFactor; j--) {
            // any products larger than current best for this i?
            product = i * j;
            if (product <= best_answer)
                break;

            if (common::isPalindrome(product)) {
                best_answer = product;
                break;
            }
        }
    }

    cout << best_answer << endl;
    return 0;
}
