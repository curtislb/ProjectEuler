/*
 * problem013.cpp
 * 
 * Problem 13: Large sum
 *
 * Work out the first D digits of the sum of the numbers contained in the file
 * INPUT_FILE (all of which have the same number of digits).
 * 
 * Author: Curtis Belmonte
 * Created: Aug 25, 2014
 */

#include <fstream>
#include <iostream>

#include <stdlib.h>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned int D = 10; // default: 10
static const char *INPUT_FILE = "input/013.txt"; // default: "input/013.txt"

/* SOLUTION ******************************************************************/

int main() {
    ifstream input(INPUT_FILE);
    if (!input.is_open()) {
        // failed to open the input file
        cout << "Unable to open file: " << INPUT_FILE << endl;
        return EXIT_FAILURE;
    }

    // read and sum all lines of the input file
    string line;
    common::BigInteger *bigint;
    common::BigInteger sum("0");
    while (getline(input, line)) {
        bigint = new common::BigInteger(line);
        sum += *bigint;
        delete bigint;
    }

    // print only the first D digits of the sum
    cout << sum.asString().substr(0, D) << endl;

    return 0;
}
