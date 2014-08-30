/*
 * problem020.cpp
 * 
 * Problem 20: Factorial digit sum
 *
 * n! means n × (n − 1) × ... × 3 × 2 × 1
 *
 * For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the
 * digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
 *
 * Find the sum of the digits in the number N!
 * 
 * Author: Curtis Belmonte
 * Created: Aug 29, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const common::Natural N = 100; // default: 100

/* SOLUTION ******************************************************************/

int main() {
    const common::BigInteger kBigN(N);
    const common::BigInteger kResult = common::factorial(kBigN);
    const common::BigInteger kDigitSum = common::sumDigits(kBigN);
    cout << kDigitSum.toString() << endl;
    return 0;
}
