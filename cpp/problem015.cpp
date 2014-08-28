/*
 * problem015.cpp
 * 
 * Problem 15: Lattice paths
 *
 * Starting in the top left corner of a 2×2 grid, and only being able to move
 * to the right and down, there are exactly 6 routes to the bottom right
 * corner.
 *
 * How many such routes are there through an N × N grid?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 26, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned short N = 20; // default: 20

/* SOLUTION ******************************************************************/

int main() {
    // compute the value of (2*N)! / N! = (2*N) * (2*N - 1) * ... * 1
    const unsigned short kMaxFactor = N * 2;
    common::BigInteger product("1");
    for (unsigned int i = N + 1; i <= kMaxFactor; i++) {
        product *= i;
    }

    // divide the numerator by N! to account for all duplicate moves
    common::BigInteger divisor = common::BigInteger(common::factorial(N));
    common::BigInteger quotient = product / divisor;

    cout << quotient.asString() << endl;
    return 0;
}