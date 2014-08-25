/*
 * problem005.cpp
 * 
 * Problem 5: Smallest multiple
 *
 * 2520 is the smallest number that can be divided by each of the numbers from
 * 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the
 * numbers from 1 to MAX?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 21, 2014
 */

#include <iostream>
#include <vector>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned int MAX = 20; // default: 20

/* SOLUTION ******************************************************************/

int main() {
    vector<common::Natural> nums(MAX - 1);
    for (unsigned int i = 2; i <= MAX; i++)
        nums[i - 2] = i;
    cout << common::lcm(nums) << endl;
    return 0;
}
