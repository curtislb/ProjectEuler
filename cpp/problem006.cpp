/*
 * problem006.cpp
 * 
 * Problem 6: Sum square difference
 *
 * The sum of the squares of the first ten natural numbers is,
 *
 *     1^2 + 2^2 + ... + 10^2 = 385
 *
 * The square of the sum of the first ten natural numbers is,
 *
 *     (1 + 2 + ... + 10)^2 = 55^2 = 3025
 *
 * Hence the difference between the sum of the squares of the first ten natural
 * numbers and the square of the sum is 3025 − 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first N natural
 * numbers and the square of the sum.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 22, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned int N = 100; // default: 100

/* SOLUTION ******************************************************************/

int main() {
    const common::Natural kSum = common::triangle(N);
    cout << kSum*kSum - common::sumOfSquares(N) << endl;
    return 0;
}
