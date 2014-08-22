/*
 * problem003.cpp
 * 
 * Problem 3: Largest prime factor
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number N?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 19, 2014
 */

#include <iostream>

#include <math.h>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const long long N = 600851475143; // default: 600851475143

/* SOLUTION ******************************************************************/

int main() {
    // generate potential prime factors of N
    const vector<common::Natural> kPrimes = common::primesUpTo(sqrt(N));

    // search for largest prime factor <= sqrt(N)
    unsigned int i;
    for (i = kPrimes.size() - 1; i > 0; i--) {
        if (N % kPrimes[i] == 0)
            break;
    }

    cout << kPrimes[i] << endl;
    return 0;
}
