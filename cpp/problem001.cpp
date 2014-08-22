/*
 * problem001.cpp
 * 
 * Problem 1: Multiples of 3 and 5
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of M or N below LIMIT.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS *****************************************************************/

static const int M = 3; // default: 3
static const int N = 5; // default: 5
static const int LIMIT = 1000; // default: 1000

/* SOLUTION *******************************************************************/

/* Returns the sum of natural numbers below LIMIT that are divisible by n. */
static int sumDivisibleBy(int n) {
    return common::arithSeries(n, (LIMIT - 1) / n, n);
}

int main() {
    int lcm = common::lcm(M, N);
    cout << sumDivisibleBy(M) + sumDivisibleBy(N) - sumDivisibleBy(lcm) << endl;
    return 0;
}
