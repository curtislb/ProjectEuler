/*
 * problem009.cpp
 * 
 * Problem 9: Special Pythagorean triplet
 *
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for
 * which,
 *
 *     a^2 + b^2 = c^2
 *
 * For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 *
 * There exists exactly one Pythagorean triplet for which a + b + c = S.
 *
 * Find the product a*b*c.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 24, 2014
 */

#include <iostream>

#include <math.h>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

const common::Natural S = 1000; // default: 1000

/* SOLUTION ******************************************************************/

int main() {
    // no triplet exists if S is not even
    if (S % 2 != 0) {
        cout << "No such triplet" << endl;
        return 0;
    }

    // let a = 2*m*n, b = m^2 - n^2, c = m^2 + n^2. Then, m^2 + m*n = S/2
    const common::Natural kSDiv2 = S / 2;
    const common::Natural kMLimit = ceil(sqrt(kSDiv2));

    // search for m and n under conditions m > n and m % 2 != n % 2
    common::Natural s_div_2m, m2, n2;
    for (common::Natural m = 2; m < kMLimit; m++) {
        if (S % m == 0) {
            s_div_2m = kSDiv2 / m;
            for (common::Natural n = (m % 2 == 0) ? 1 : 2; n < m; n += 2) {
                if (m + n == s_div_2m) {
                    // compute a, b, and c from the definitions of m and n
                    m2 = m * m;
                    n2 = n * n;
                    cout << (2 * m * n) * (m2 - n2) * (m2 + n2) << endl;
                    return 0;
                }
            }
        }
    }

    return 0;
}
