/*
 * problem067.cpp
 * 
 * Problem 67: Maximum path sum II
 *
 * By starting at the top of the triangle below and moving to adjacent numbers
 * on the row below, the maximum total from top to bottom is 23.
 *
 *        3
 *       7 4
 *      2 4 6
 *     8 5 9 3
 *
 * That is, 3 + 7 + 4 + 9 = 23.
 *
 * Find the maximum total from top to bottom in the triangle contained in the
 * file INPUT_FILE.
 *
 * NOTE: This is a much more difficult version of Problem 18. It is not
 * possible to try every route to solve this problem, as there are 2^99
 * altogether! If you could check one trillion (10^12) routes every second it
 * would take over twenty billion years to check them all. There is an
 * efficient algorithm to solve it.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 29, 2014
 */

#include <iostream>
#include <vector>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const char *IN_FILE = "../input/067.txt"; // default: "../input/067.txt"

/* SOLUTION ******************************************************************/

int main() {
    vector<vector<long> > triangle = common::numbersFromFile(IN_FILE);
    cout << common::maxTrianglePath(triangle) << endl;
    return 0;
}
