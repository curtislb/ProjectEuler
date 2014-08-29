/*
 * problem017.cpp
 * 
 * Problem 17: Number letter counts
 *
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 * then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 *
 * If all the numbers from 1 to 1000 (one thousand), inclusive were written out
 * in words, how many letters would be used?
 *
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
 * forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
 * letters. The use of "and" when writing out numbers is in compliance with
 * British usage.
 * 
 * Author: Curtis Belmonte
 * Created: Aug 29, 2014
 */

#include <iostream>

//#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

// TODO: parameterize upper limit

/* SOLUTION ******************************************************************/

int main() {
    // compute the sum of all digit letter counts, excluding 0
    const unsigned int kAllDigitLetters =
            3 // strlen("one")
          + 3 // strlen("two")
          + 5 // strlen("three")
          + 4 // strlen("four")
          + 4 // strlen("five")
          + 3 // strlen("six")
          + 5 // strlen("seven")
          + 5 // strlen("eight")
          + 4 // strlen("nine")
    ;

    // compute the sum of all "teen" letter counts, including 10, 11, and 12
    const unsigned int kAllTeenLetters =
            3 // strlen("ten")
          + 6 // strlen("eleven")
          + 6 // strlen("twelve")
          + 8 // strlen("thirteen")
          + 8 // strlen("fourteen")
          + 7 // strlen("fifteen")
          + 7 // strlen("sixteen")
          + 9 // strlen("seventeen")
          + 8 // strlen("eighteen")
          + 8 // strlen("nineteen")
     ;

    // compute the sum of all multiples of ten letter counts, excluding 10
    const unsigned int kAllTenLetters =
            6 // strlen("twenty")
          + 6 // strlen("thirty")
          + 5 // strlen("forty")
          + 5 // strlen("fifty")
          + 5 // strlen("sixty")
          + 7 // strlen("seventy")
          + 6 // strlen("eighty")
          + 6 // strlen("ninety")
     ;

    // count the letters of other useful number words
    const unsigned int kAndLetters = 3; // strlen("and");
    const unsigned int kHundredLetters = 7; // strlen("hundred");
    const unsigned int kOneLetters = 3; // strlen("one");
    const unsigned int kThousandLetters = 8; // strlen("thousand");

    // count the letters of all numbers below 20
    unsigned int letter_count = kAllDigitLetters + kAllTeenLetters;

    // count the letters of all numbers from 20 to 99
    const unsigned int kDigitCount = 9;
    const unsigned int kTenCount = 8;
    letter_count += (kAllTenLetters * (kDigitCount + 1))
                    + (kAllDigitLetters * kTenCount);
    const unsigned int kLettersBelow100 = letter_count;

    // count the letters of all numbers from 100 to 999
    const unsigned int kNumbersBelow100 = 99;
    const unsigned int kAndWordCount = kDigitCount * kNumbersBelow100;
    const unsigned int kHundredWordCount = kAndWordCount + kDigitCount;
    letter_count += (kAllDigitLetters * (kNumbersBelow100 + 1))
                    + (kHundredLetters * kHundredWordCount)
                    + (kAndLetters * kAndWordCount)
                    + (kLettersBelow100 * kDigitCount);

    // count the letters of 1000
    letter_count += kOneLetters + kThousandLetters;

    cout << letter_count << endl;
    return 0;
}
