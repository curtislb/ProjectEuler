/*
 * problem016.cpp
 * 
 * Problem 16: Power digit sum
 *
 * 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
 *
 * What is the sum of the digits of the number BASE^EXPONENT?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 28, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const common::Natural BASE = 2; // default: 2
static const common::Natural EXPONENT = 1000; // default: 1000

/* SOLUTION ******************************************************************/

int main() {
    const common::BigInteger kBigBase(BASE);
    const common::BigInteger kBigExponent(EXPONENT);
    const common::BigInteger kResult = kBigBase.power(kBigExponent);
    const common::BigInteger kDigitSum = common::sumDigits(kResult);
    cout << kResult.toString() << endl;
    return 0;
}
