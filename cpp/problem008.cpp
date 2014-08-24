/*
 * problem008.cpp
 * 
 * Problem 8: Largest product in a series
 *
 * The four adjacent digits in the 1000-digit number that have the greatest
 * product are 9 × 9 × 8 × 9 = 5832.
 *
 *     73167176531330624919225119674426574742355349194934
 *     96983520312774506326239578318016984801869478851843
 *     85861560789112949495459501737958331952853208805511
 *     12540698747158523863050715693290963295227443043557
 *     66896648950445244523161731856403098711121722383113
 *     62229893423380308135336276614282806444486645238749
 *     30358907296290491560440772390713810515859307960866
 *     70172427121883998797908792274921901699720888093776
 *     65727333001053367881220235421809751254540594752243
 *     52584907711670556013604839586446706324415722155397
 *     53697817977846174064955149290862569321978468622482
 *     83972241375657056057490261407972968652414535100474
 *     82166370484403199890008895243450658541227588666881
 *     16427171479924442928230863465674813919123162824586
 *     17866458359124566529476545682848912883142607690042
 *     24219022671055626321111109370544217506941658960408
 *     07198403850962455444362981230987879927244284909188
 *     84580156166097919133875499200524063689912560717606
 *     05886116467109405077541002256983155200055935729725
 *     71636269561882670428252483600823257530420752963450
 *
 * Find the N adjacent digits in the number contained in the file INPUT_FILE
 * that have the greatest product. What is the value of this product?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 23, 2014
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const unsigned int N = 13;
static const char *INPUT_FILE = "input/008.txt";

/* SOLUTION ******************************************************************/

int main() {
    ifstream input(INPUT_FILE);
    if (input.is_open()) {
        // read number from input file
        string number_string;
        getline(input, number_string);
        input.close();

        // store digits of number in vector
        vector<int> digits;
        const unsigned int kDigitCount = number_string.size();
        digits.reserve(kDigitCount);
        for (unsigned int i = 0; i < kDigitCount; i++)
            digits[i] = common::charToDigit(number_string[i]);

        unsigned int num_zeros = 0; // number of zeros in the current product
        common::Natural product = 1; // current product of N digits (ignore 0)
        common::Natural max_product = 0; // largest product of N digits

        // compute product of initial N digits
        unsigned int i;
        for (i = 0; i < N; i++) {
            if (digits[i] == 0)
                num_zeros++;
            else
                product *= digits[i];
        }

        // compute products of remaining sets of N digits
        while (i < kDigitCount) {
            // remove leftmost digits from product
            if (digits[i - N] == 0)
                num_zeros--;
            else
                product /= digits[i - N];

            // add new rightmost digit to product
            if (digits[i] == 0)
                num_zeros++;
            else
                product *= digits[i];

            // if any zeros in product, treat it as 0
            if (num_zeros == 0 && product > max_product)
                max_product = product;

            i++;
        }

        cout << max_product << endl;

    } else {
        // failed to open the input file
        cout << "Unable to open file: " << INPUT_FILE << endl;
    }

    return 0;
}
