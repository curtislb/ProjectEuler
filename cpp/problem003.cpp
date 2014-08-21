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

#include "common.h"

using namespace std;

/* PARAMETERS *****************************************************************/

static const long N = 600851475143L; // default: 600851475143L

/* FUNCTIONS ******************************************************************/



/* SOLUTION *******************************************************************/

int main () {
    common::computePrimesUpTo(60);
    common::computePrimesUpTo(120);
    for (int i = 0; i < 30; i++) {
        cout << common::prime(i) << endl;
    }
    return 0;
}
