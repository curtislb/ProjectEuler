/*
 * problem010.cpp
 * 
 * Problem 10: Summation of primes
 *
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below N.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 24, 2014
 */

#include <iostream>
#include <numeric>
#include <vector>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const common::Natural N = 2000000; // default: 2000000

/* SOLUTION ******************************************************************/

int main() {
    const vector<common::Natural> kPrimes = common::primesUpTo(N);
    cout << accumulate(kPrimes.begin(), kPrimes.end(), 0) << endl;
    return 0;
}
