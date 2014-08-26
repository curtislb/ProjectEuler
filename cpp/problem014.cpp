/*
 * problem014.cpp
 * 
 * Problem 14: Longest Collatz sequence
 *
 * The following iterative sequence is defined for the set of positive
 * integers:
 *
 *     n → n/2 (n is even)
 *     n → 3n + 1 (n is odd)
 *
 * Using the rule above and starting with 13, we generate the following
 * sequence:
 *
 *     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 *
 * It can be seen that this sequence (starting at 13 and finishing at 1)
 * contains 10 terms. Although it has not been proved yet (Collatz Problem), it
 * is thought that all starting numbers finish at 1.
 *
 * Which starting number, under LIMIT, produces the longest chain?
 *
 * NOTE: Once the chain starts the terms are allowed to go above one million.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 26, 2014
 */

#include <iostream>
#include <map>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

static const common::Natural LIMIT = 1000000; // default: 1000000

/* SOLUTION ******************************************************************/

/* Memoized vector of previously computed Collatz sequence lengths. */
static map<common::Natural, common::Natural> collatz_lengths;

/* Returns the number of terms in the Collatz sequence starting from n. */
inline static common::Natural collatzLength(common::Natural n) {
    // base case
    if (n == 1)
        return 1;

    // return the memoized result
    if (collatz_lengths.count(n))
        return collatz_lengths[n];

    // compute and memoize the length of the rest of the sequence + 1
    return collatz_lengths[n] = 1 + collatzLength(common::collatzStep(n));
}

int main() {
    // search for longest Collatz sequence starting below LIMIT
    common::Natural best_num = 0;
    common::Natural best_length = 0;
    common::Natural length;
    for (common::Natural i = 1; i < LIMIT; i++) {
        // compute the length of the sequence starting from i
        length = collatzLength(i);
        if (length > best_length) {
            best_num = i;
            best_length = length;
        }
    }

    cout << best_num << endl;
    return 0;
}
