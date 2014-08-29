/*
 * common.cpp
 *
 * Common utility functions and classes for various Project Euler problems.
 *
 * Author: Curtis Belmonte
 * Created: Aug 18, 2014
 */

#include <algorithm>
#include <climits>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <utility>
#include <vector>

#include <math.h>
#include <stdlib.h>

#include "common.h"

using namespace std;

namespace common {

/* STATIC CONSTANTS **********************************************************/

    /* BigInteger constant representing the number 1. */
    static const BigInteger BIG_ONE("1");

    /* BigInteger constant representing the number 0. */
    static const BigInteger BIG_ZERO("0");

    /* Number of digits at which Karatsuba multiplication is carried out. */
    static const unsigned int KARATSUBA_CUTOFF = 2;

/* STATIC VARIABLES **********************************************************/

    /* Currently computed terms of the Fibonacci sequence (in sorted order). */
    static vector<Natural> fibonacci_sequence(2, 1);

    /* Currently computed prime number terms (in sorted order). */
    static vector<Natural> prime_sequence(1, 2);

/* STATIC FUNCTIONS **********************************************************/

    /*** Declarations ***/

    /* Precomputes and stores the first n Fibonacci numbers. */
    static void computeFibonacci(unsigned int n);

    /* Precomputes and stores the Fibonacci numbers up to at least n. */
    static void computeFibonacciUpTo(Natural n);

    /* Precomputes and stores the first n prime numbers. */
    static void computePrimes(unsigned int n);

    /* Precomputes and stores the prime numbers up to n. */
    static void computePrimesUpTo(Natural n);

    /*
     * Returns the sum of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitAdd(const vector<short> m_digits_copy,
                                  const vector<short> n_digits_copy);

    /*
     * Compares the natural numbers m and n, represented as vectors of their
     * digits m_digits and n_digits, respectively. Returns a positive value if
     * m > n, a negative value if m < n, or 0 if m == n.
     */
    static int digitCompare(const vector<short> m_digits_copy,
                            const vector<short> n_digits_copy);

    /*
     * Returns the integer quotient of two natural numbers m and n, represented
     * as vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitDivide(const vector<short> m_digits,
                                     const vector<short> n_digits);

    /*
     * Returns the product of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitMultiply(const vector<short> m_digits_copy,
                                       const vector<short> n_digits_copy);

    /*
     * Returns the difference of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively. Assumes
     * that m is greater than or equal to n.
     */
    static vector<short> digitSubtract(const vector<short> m_digits_copy,
                                       const vector<short> n_digits_copy);

    /* Returns a copy of the digit vector digits with leading zeros removed. */
    static vector<short> digitTrim(const vector<short> digits);

    /*** Implementations ***/

    /* Precomputes and stores the Fibonacci numbers up to F(n). */
    static void computeFibonacci(unsigned int n) {
        const unsigned int kFibCount = fibonacci_sequence.size();

        // have the numbers up to F(n) already been computed?
        if (n < kFibCount)
            return;

        // make room for numbers to be added to sequence
        fibonacci_sequence.reserve(n + 1);

        // compute numbers iteratively from existing sequence
        Natural f0 = fibonacci_sequence[kFibCount - 2];
        Natural f1 = fibonacci_sequence[kFibCount - 1];
        Natural temp;
        for (unsigned int count = kFibCount; count <= n; count++) {
            temp = f1;
            f1 += f0;
            f0 = temp;
            fibonacci_sequence.push_back(f1);
        }
    }

    /* Precomputes and stores the Fibonacci numbers up to at least n. */
    static void computeFibonacciUpTo(Natural n) {
        const unsigned int kFibCount = fibonacci_sequence.size();

        // have the numbers up to f already been computed?
        if (fibonacci_sequence[kFibCount - 1] >= n)
            return;

        // compute numbers iteratively from existing sequence
        Natural f0 = fibonacci_sequence[kFibCount - 2];
        Natural f1 = fibonacci_sequence[kFibCount - 1];
        Natural temp;
        while (f1 < n) {
            temp = f1;
            f1 += f0;
            f0 = temp;
            fibonacci_sequence.push_back(f1);
        }
    }

    /* Precomputes and stores the first n prime numbers. */
    static void computePrimes(unsigned int n) {
        unsigned int kPrimeCount = prime_sequence.size();

        // have the first n primes already been computed?
        if (n < kPrimeCount)
            return;

        // TODO: implement incremental sieve?

        // based on analysis of OEIS data set A006880 and empirical time tests
        const Natural kEstimate = (n <= 25) ? 100 : (n*log(n)*1.05 + n*0.87);
        const Natural kIncrement = n / log(n);

        // compute primes up to estimate, then step forward until n are found
        for (Natural i = kEstimate; prime_sequence.size() < n; i += kIncrement)
            computePrimesUpTo(i);
    }

    /* Precomputes and stores the prime numbers up to n. */
    static void computePrimesUpTo(Natural n) {
        const unsigned int kPrimeCount = prime_sequence.size();

        // have the numbers up to p already been computed?
        Natural prime_max = prime_sequence[kPrimeCount - 1];
        if (prime_max >= n)
            return;

        // prepare sieve of Eratosthenes for numbers prime_max+1 to p
        const unsigned int kSieveSize = n - prime_max;
        vector<bool> sieve(kSieveSize, true);

        // sift out composite numbers using previously computed primes
        Natural rho;
        for (unsigned int i = 0; i < kPrimeCount; i++) {
            rho = prime_sequence[i];
            for (Natural j = rho*rho; j < kSieveSize + prime_max + 1; j += rho) {
                if (j < prime_max + 1)
                    continue;
                sieve[j - prime_max - 1] = false;
            }
        }

        // sift out remaining composite numbers with newly found primes
        for (unsigned int i = 0; i < kSieveSize; i++) {
            if (sieve[i]) {
                rho = i + prime_max + 1;
                prime_sequence.push_back(rho);
                for (Natural j = rho*rho - prime_max - 1; j < kSieveSize; j += rho)
                    sieve[j] = false;
            }
        }
    }

    /*
     * Returns the sum of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitAdd(const vector<short> m_digits,
                                  const vector<short> n_digits) {
        // copy values from read-only argument vectors to writable ones
        vector<short> m_digits_copy(m_digits.begin(), m_digits.end());
        vector<short> n_digits_copy(n_digits.begin(), n_digits.end());

        // count the number of digits of m and n
        const unsigned int kMDigitCount = m_digits_copy.size();
        const unsigned int kNDigitCount = n_digits_copy.size();
        const unsigned int kMaxDigitCount = max(kMDigitCount, kNDigitCount);

        // pad the digits of m and n to be the same length
        if (kMDigitCount > kNDigitCount) {
            // pad n with zeros until it is the same length as m
            vector<short> n_digits_padded(kMDigitCount, 0);
            copy(n_digits_copy.begin(), n_digits_copy.end(),
                 n_digits_padded.begin() + (kMDigitCount - kNDigitCount));
            n_digits_copy = n_digits_padded;
        } else if (kMDigitCount < kNDigitCount) {
            // pad m with zeros until it is the same length as n
            vector<short> m_digits_padded(kNDigitCount, 0);
            copy(m_digits_copy.begin(), m_digits_copy.end(),
                 m_digits_padded.begin() + (kNDigitCount - kMDigitCount));
            m_digits_copy = m_digits_padded;
        }

        vector<short> sum; // the sum of m and n
        bool carry_digit = 0; // digit carried over from the previous addition

        // add the digits of m and n
        unsigned int i;
        short m_digit, n_digit, digit_sum;
        for (i = 0; i < kMaxDigitCount; i++) {
            // add both digits and the carry digit from the last addition
            m_digit = m_digits_copy[kMaxDigitCount - 1 - i];
            n_digit = n_digits_copy[kMaxDigitCount - 1 - i];
            digit_sum = m_digit + n_digit + carry_digit;

            // split the result into a digit of sum and a carry digit
            sum.push_back(digit_sum % 10);
            carry_digit = static_cast<bool>(digit_sum / 10);
        }

        if (carry_digit) {
            // carry over final digit into new column
            sum.push_back(carry_digit);
        }

        // reverse the digits of sum, so that they are in the correct order
        reverse(sum.begin(), sum.end());

        return sum;
    }

    /*
     * Compares the natural numbers m and n, represented as vectors of their
     * digits m_digits and n_digits, respectively. Returns a positive value if
     * m > n, a negative value if m < n, or 0 if m == n.
     */
    int digitCompare(const vector<short> m_digits,
                     const vector<short> n_digits) {
        // copy values from read-only argument vectors to writable ones
        vector<short> m_digits_copy(m_digits.begin(), m_digits.end());
        vector<short> n_digits_copy(n_digits.begin(), n_digits.end());

        // count the digits of m and n
        const unsigned int kMDigitCount = m_digits_copy.size();
        const unsigned int kNDigitCount = n_digits_copy.size();
        const unsigned int kMaxDigitCount = max(kMDigitCount, kNDigitCount);

        // pad the digits of m and n to be the same length
        if (kMDigitCount > kNDigitCount) {
            // pad n with zeros until it is the same length as m
            vector<short> n_digits_padded(kMDigitCount, 0);
            copy(n_digits_copy.begin(), n_digits_copy.end(),
                 n_digits_padded.begin() + (kMDigitCount - kNDigitCount));
            n_digits_copy = n_digits_padded;
        } else if (kMDigitCount < kNDigitCount) {
            // pad m with zeros until it is the same length as n
            vector<short> m_digits_padded(kNDigitCount, 0);
            copy(m_digits_copy.begin(), m_digits_copy.end(),
                 m_digits_padded.begin() + (kNDigitCount - kMDigitCount));
            m_digits_copy = m_digits_padded;
        }

        // starting with high-order digits, check for inequality of m and n
        for (unsigned int i = 0; i < kMaxDigitCount; i++) {
            if (m_digits_copy[i] > n_digits_copy[i])
                return 1;
            if (m_digits_copy[i] < n_digits_copy[i])
                return -1;
        }

        // no inequality found; m and n must be equal
        return 0;
    }

    /*
     * Returns the integer quotient of two natural numbers m and n, represented
     * as vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitDivide(const vector<short> m_digits,
                                     const vector<short> n_digits) {
        vector<short> quotient(1, 0);

        // return 1 or 0 if n >= m
        int comparison = digitCompare(m_digits, n_digits);
        if (comparison <= 0) {
            quotient[0] = !comparison;
            return quotient;
        }

        // trim and copy the digits of m and n simultaneously
        vector<short> m_digits_copy = digitTrim(m_digits);
        vector<short> n_digits_copy = digitTrim(n_digits);

        // count the digits of m and n
        const unsigned int kMDigits = m_digits_copy.size();
        const unsigned int kNDigits = n_digits_copy.size();

        // shift divisor n left by appending zeros
        unsigned int i;
        for (i = 1; i <= kMDigits - kNDigits; i++)
            n_digits_copy.push_back(0);

        // compute the quotient using long division
        short q_digit;
        do {
            // count the number of times n divides m in the current place
            q_digit = 0;
            while (digitCompare(m_digits_copy, n_digits_copy) >= 0) {
                m_digits_copy = digitSubtract(m_digits_copy, n_digits_copy);
                q_digit++;
            }

            // append a digit of the quotient and shift the divisor right
            quotient.push_back(q_digit);
            n_digits_copy.pop_back();
            i--;
        } while (i > 0);

        return quotient;
    }

    /*
     * Returns the product of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively.
     */
    static vector<short> digitMultiply(const vector<short> m_digits,
                                       const vector<short> n_digits) {
        // copy values from read-only argument vectors to writable ones
        vector<short> m_digits_copy(m_digits.begin(), m_digits.end());
        vector<short> n_digits_copy(n_digits.begin(), n_digits.end());

        // count the digits of m and n
        const unsigned int kMDigitCount = m_digits_copy.size();
        const unsigned int kNDigitCount = n_digits_copy.size();
        const unsigned int kMaxDigitCount = max(kMDigitCount, kNDigitCount);

        // pad the digits of m and n to be the same length
        if (kMDigitCount > kNDigitCount) {
            // pad n with zeros until it is the same length as m
            vector<short> n_digits_padded(kMDigitCount, 0);
            copy(n_digits_copy.begin(), n_digits_copy.end(),
                 n_digits_padded.begin() + (kMDigitCount - kNDigitCount));
            n_digits_copy = n_digits_padded;
        } else if (kMDigitCount < kNDigitCount) {
            // pad m with zeros until it is the same length as n
            vector<short> m_digits_padded(kNDigitCount, 0);
            copy(m_digits_copy.begin(), m_digits_copy.end(),
                 m_digits_padded.begin() + (kNDigitCount - kMDigitCount));
            m_digits_copy = m_digits_padded;
        }

        // base case: if m and n are sufficiently small, multiply them normally
        if (kMaxDigitCount < KARATSUBA_CUTOFF) {
            Natural m = digitsToNumber(m_digits_copy);
            Natural n = digitsToNumber(n_digits_copy);
            return numberToDigits(m * n);
        }

        // compute the offset that will be used to split the digits
        const unsigned int kSplitOffset = kMaxDigitCount / 2;
        const unsigned int kCeilSplitOffset = (kMaxDigitCount + 1) / 2;

        // split m into high- and low-order digits
        vector<short>::iterator m_begin = m_digits_copy.begin();
        vector<short>::iterator m_mid = m_begin + kCeilSplitOffset;
        vector<short>::iterator m_end = m_digits_copy.end();
        vector<short> m_high(m_begin, m_mid);
        vector<short> m_low(m_mid, m_end);

        // split n into high- and low-order digits
        vector<short>::iterator n_begin = n_digits_copy.begin();
        vector<short>::iterator n_mid = n_begin + kCeilSplitOffset;
        vector<short>::iterator n_end = n_digits_copy.end();
        vector<short> n_high(n_begin, n_mid);
        vector<short> n_low(n_mid, n_end);

        // compute three sub-products recursively
        const vector<short> k0 = digitMultiply(m_high, n_high);
        const vector<short> k1 = digitMultiply(digitAdd(m_high, m_low),
                                               digitAdd(n_high, n_low));
        const vector<short> k2 = digitMultiply(m_low, n_low);

        // compute the "z" terms of the Karatsuba algorithm
        const vector<short> z0 = k0;
        const vector<short> z1 = digitSubtract(k1, digitAdd(k0, k2));
        const vector<short> z2 = k2;

        // pad z0 with zeros to simulate multiplication by 10^(2*kSplitOffset)
        vector<short> z0_product(z0.size() + (kSplitOffset * 2), 0);
        copy(z0.begin(), z0.end(), z0_product.begin());

        // pad z1 with zeros to simulate multiplication by 10^(kSplitOffset)
        vector<short> z1_product(z1.size() + kSplitOffset, 0);
        copy(z1.begin(), z1.end(), z1_product.begin());

        return digitAdd(digitAdd(z0_product, z1_product), z2);
    }

    /*
     * Returns the difference of two natural numbers m and n, represented as
     * vectors of their digits m_digits and n_digits, respectively. Assumes
     * that m is greater than or equal to n.
     */
    static vector<short> digitSubtract(const vector<short> m_digits,
                                       const vector<short> n_digits) {
        // copy values from read-only argument vectors to writable ones
        vector<short> m_digits_copy(m_digits.begin(), m_digits.end());
        vector<short> n_digits_copy(n_digits.begin(), n_digits.end());

        // count the number of digits of m and n
        const unsigned int kMDigitCount = m_digits_copy.size();
        const unsigned int kNDigitCount = n_digits_copy.size();
        const unsigned int kMaxDigitCount = max(kMDigitCount, kNDigitCount);

        // pad the digits of m and n to be the same length
        if (kMDigitCount > kNDigitCount) {
            // pad n with zeros until it is the same length as m
            vector<short> n_digits_padded(kMDigitCount, 0);
            copy(n_digits_copy.begin(), n_digits_copy.end(),
                 n_digits_padded.begin() + (kMDigitCount - kNDigitCount));
            n_digits_copy = n_digits_padded;
        } else if (kMDigitCount < kNDigitCount) {
            // pad m with zeros until it is the same length as n
            vector<short> m_digits_padded(kNDigitCount, 0);
            copy(m_digits_copy.begin(), m_digits_copy.end(),
                 m_digits_padded.begin() + (kNDigitCount - kMDigitCount));
            m_digits_copy = m_digits_padded;
        }

        vector<short> diff; // the difference of m and n
        bool borrow_digit = 0; // digit borrowed for subtraction

        // subtract the digits of n from m
        unsigned int i;
        short m_digit, n_digit, digit_diff;
        for (i = 0; i < kMaxDigitCount; i++) {
            // get m and n digit of current column, accounting for borrowing
            m_digit = m_digits_copy[kMaxDigitCount - 1 - i] - borrow_digit;
            n_digit = n_digits_copy[kMaxDigitCount - 1 - i];

            // subtract this digit of n from that of n, borrowing if necessary
            borrow_digit = m_digit < n_digit;
            digit_diff = m_digit + (borrow_digit * 10) - n_digit;
            diff.push_back(digit_diff);
        }

        // reverse the digits of diff, so that they are in the right order
        reverse(diff.begin(), diff.end());

        return diff;
    }

    /* Returns a copy of the digit vector digits with leading zeros removed. */
    static vector<short> digitTrim(const vector<short> digits) {
        // advance beginning iterator past leading zeros
        vector<short>::const_iterator digits_begin = digits.begin();
        while (*digits_begin == 0 && digits_begin != digits.end())
            ++digits_begin;

        // if iterator reaches end, number must be zero; correct by one place
        if (digits_begin == digits.end())
            --digits_begin;

        // copy the digits starting after leading zeros
        vector<short> digits_trimmed(digits_begin, digits.end());
        return digits_trimmed;
    }

/* CLASS METHODS *************************************************************/

    /*** BigInteger ***/

    /* Constructs a new BigInteger. */
    BigInteger::BigInteger() {
        // do nothing
    }

    /* Constructs a new BigInteger that is a copy of big_int. */
    BigInteger::BigInteger(const BigInteger &big_int) {
        vector<short> big_int_digits_copy(big_int.digits.begin(), big_int.digits.end());
        digits = big_int_digits_copy;
    }

    /*
     * Constructs a BigInteger from its numerical representation as a decimal
     * integer in the C-style string int_string.
     */
    BigInteger::BigInteger(const char *int_string) {
        for (Natural i = 0; int_string[i] != '\0'; i++)
            digits.push_back(charToDigit(int_string[i]));
    }

    /*
     * Constructs a BigInteger from its numerical representation as a decimal
     * integer in the string int_string.
     */
    BigInteger::BigInteger(string int_string) {
        const Natural kStringSize = int_string.size();
        for (Natural i = 0; i < kStringSize; i++)
            digits.push_back(charToDigit(int_string[i]));
    }

    /* Constructs a BigInteger from the natural number n. */
    BigInteger::BigInteger(Natural n) {
        // convert n to a string
        ostringstream n_oss;
        n_oss << n;
        const string kIntString = n_oss.str();
        const unsigned int kStringSize = kIntString.size();

        // construct the BigInteger normally from the string
        for (unsigned int i = 0; i < kStringSize; i++)
            digits.push_back(charToDigit(kIntString[i]));
    }

    /* Returns the value of this BigInteger modulo 10. */
    short BigInteger::mod10() const {
        return digits[digits.size() - 1];
    }

    /* Returns the sum of this BigInteger and other. */
    BigInteger BigInteger::operator+(const BigInteger &other) const {
        BigInteger sum;
        sum.digits = digitTrim(digitAdd(digits, other.digits));
        return sum;
    }

    /* Adds the value of other to this BigInteger. */
    BigInteger &BigInteger::operator+=(const BigInteger &other) {
        return *this = *this + other;
    }

    /* Adds one to the value of this BigInteger. */
    BigInteger &BigInteger::operator++(int postfix) {
        return *this += BIG_ONE;
    }

    /* Returns the difference of this BigInteger and other. */
    BigInteger BigInteger::operator-(const BigInteger &other) const {
        BigInteger diff;
        diff.digits = digitTrim(digitSubtract(digits, other.digits));
        return diff;
    }

    /* Subtracts the value of other from this BigInteger. */
    BigInteger &BigInteger::operator-=(const BigInteger &other) {
        return *this = *this - other;
    }

    /* Adds one to the value of this BigInteger. */
    BigInteger &BigInteger::operator--(int postfix) {
        return *this -= BIG_ONE;
    }

    /* Returns the product of this BigInteger and other. */
    BigInteger BigInteger::operator*(const BigInteger &other) const {
        BigInteger product;
        product.digits = digitTrim(digitMultiply(digits, other.digits));
        return product;
    }

    /* Multiplies this BigInteger by the value of other. */
    BigInteger &BigInteger::operator*=(const BigInteger &other) {
        return *this = *this * other;
    }

    /* Returns the value of this BigInteger divided by other. */
    BigInteger BigInteger::operator/(const BigInteger &other) const {
        BigInteger quotient;
        quotient.digits = digitTrim(digitDivide(digits, other.digits));
        return quotient;
    }

    /* Divides the value of this BigInteger by other. */
    BigInteger &BigInteger::operator/=(const BigInteger &other) {
        return *this = *this / other;
    }

    /* Determines if this BigInteger is less than other. */
    bool BigInteger::operator<(const BigInteger &other) const {
        return digitCompare(digits, other.digits) < 0;
    }

    /* Determines if this BigInteger is less than or equal to other. */
    bool BigInteger::operator<=(const BigInteger &other) const {
        return digitCompare(digits, other.digits) <= 0;
    }

    /* Determines if this BigInteger is greater than other. */
    bool BigInteger::operator>(const BigInteger &other) const {
        return digitCompare(digits, other.digits) > 0;
    }

    /* Determines if this BigInteger is greater than or equal to other. */
    bool BigInteger::operator>=(const BigInteger &other) const {
        return digitCompare(digits, other.digits) >= 0;
    }

    /* Determines if this BigInteger is equal to other. */
    bool BigInteger::operator==(const BigInteger &other) const {
        return digitCompare(digits, other.digits) == 0;
    }

    /* Determines if this BigInteger is not equal to other. */
    bool BigInteger::operator!=(const BigInteger &other) const {
        return digitCompare(digits, other.digits) != 0;
    }

    /* Returns the value of this BigInteger raised to the n power. */
    BigInteger BigInteger::power(const BigInteger &n) const {
//        cout << "problem: " << digitsToNumber(digits) << "^" << digitsToNumber(n.digits) << endl;

        // base case: this to the 0th power equals 1
        if (n == BIG_ZERO) {
            BigInteger result("1");
            return result;
        }

        // recursively compute half power
        const BigInteger kHalfPow = this->power(n / 2);

        // compute original power
        if (n.digits[n.digits.size() - 1] % 2 == 0) {
            BigInteger product = kHalfPow * kHalfPow;
            return product;
        } else {
            BigInteger product = *this * kHalfPow * kHalfPow;
            return product;
        }
    }

    /* Returns the decimal string representation of this BigInteger. */
    string BigInteger::toString() const {
        ostringstream digits_oss;
        for (vector<short>::const_iterator i = digits.begin(); i != digits.end(); ++i)
            digits_oss << *i;
        return digits_oss.str();
    }

/* FUNCTIONS *****************************************************************/

    /*
     * Returns the sum of the arithmetic sequence with first term a, number of
     * terms n, and difference between terms d.
     */
    long long arithSeries(long long a, long long n, long long d) {
        return n * (2 * a + (n - 1) * d) / 2;
    }

    /* Returns the numeric value of character c, representing a digit 0-9.  */
    short charToDigit(char c) {
        return c - '0';
    }

    /* Returns the next number in the Collatz sequence following n. */
    Natural collatzStep(Natural n) {
        return (n % 2 == 0) ? (n / 2) : (3 * n + 1);
    }

    /* Returns the number of digits of the natural number n. */
    unsigned int countDigits(Natural n) {
        unsigned int count = 0;
        while (n != 0) {
            n /= 10;
            count++;
        }

        // if count is 0, then n must be 0, which has one digit
        return count ? count : 1;
    }

    /* Returns the number of divisors of the natural number n. */
    unsigned int countDivisors(Natural n) {
        // compute the product of one more than the powers of its prime factors
        unsigned int divisor_count = 1;
        vector<pair<Natural, unsigned int> > factors = primeFactorization(n);
        for (vector<pair<Natural, unsigned int> >::iterator i = factors.begin(); i != factors.end(); ++i)
            divisor_count *= (i->second + 1);

        return divisor_count;
    }

    /* Returns the natural number represented by the digit vector digits. */
    Natural digitsToNumber(const vector<short> digits) {
        // count the number of digits
        const unsigned int kDigitCount = digits.size();

        // add each digit (scaled by appropriate power of 10) to total
        Natural num = 0;
        Natural factor = 1;
        for (unsigned int i = 0; i < kDigitCount; i++) {
            num += digits[kDigitCount - 1 - i] * factor;
            factor *= 10;
        }

        return num;
    }

    /* Returns the factorial of n, defined as n! = n * (n - 1) * ... * 1. */
    BigInteger factorial(const BigInteger &n) {
        BigInteger product("1");
        for (BigInteger i("2"); i <= n; i++) {
            product *= i;
        }
        return product;
    }

    /* Returns the factorial of n, defined as n! = n * (n - 1) * ... * 1. */
    Natural factorial(unsigned short n) {
        Natural product = 1;
        for (unsigned short i = 2; i <= n; i++) {
            product *= i;
        }
        return product;
    }

    /* Returns the nth Fibonacci number, with F(0) = F(1) = 1. */
    Natural fibonacci(unsigned int n) {
        computeFibonacci(n);
        return fibonacci_sequence[n];
    }

    /* Returns the first n Fibonacci numbers. */
    vector<Natural> fibonacciNums(unsigned int n) {
        computeFibonacci(n);

        vector<Natural> f_list(fibonacci_sequence.begin(),
                fibonacci_sequence.begin() + n);
        return f_list;
    }

    /* Returns the Fibonacci numbers up to n. */
    vector<Natural> fibonacciNumsUpTo(Natural n) {
        computeFibonacciUpTo(n);

        // find the index of the last Fibonacci number <= n
        unsigned int i = 0;
        const unsigned int kFibCount = fibonacci_sequence.size();
        while (i < kFibCount && fibonacci_sequence[i] <= n)
            i++;

        vector<Natural> f_list(fibonacci_sequence.begin(),
                fibonacci_sequence.begin() + i);
        return f_list;
    }

    /* Returns the greatest common divisor of m and n. */
    Natural gcd(Natural m, Natural n) {
        // find gcd using Euler's method
        int temp;
        while (n != 0) {
            temp = n;
            n = m % n;
            m = temp;
        }
        return m;
    }

    /* Determines if the natural number n is a palindrome. */
    bool isPalindrome(Natural n) {
        // convert n to a string
        ostringstream n_stringstream;
        n_stringstream << n;
        string n_string = n_stringstream.str();

        // compare chars iteratively from beginning and end of string
        int i = 0;
        int j = n_string.length() - 1;
        while (i < j) {
            if (n_string[i] != n_string[j])
                return false;
            i++;
            j--;
        }
        return true;
    }

    /* Determines if the natural number n is prime. */
    bool isPrime(Natural n) {
        // simple test for small n: 2 and 3 are prime, but 1 is not
        if (n <= 3) {
            if (n <= 1)
                return false;
            return true;
        }

        // check if multiple of 2 or 3
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        // search for subsequent prime factors around multiples of 6
        const unsigned int kMaxFactor = sqrt(n);
        for (unsigned int i = 5; i <= kMaxFactor; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    /* Returns the least common multiple of m and n. */
    Natural lcm(Natural m, Natural n) {
        return m * n / gcd(m, n);
    }

    /* Returns the least common multiple of all numbers in nums. */
    Natural lcm(vector<Natural> nums) {
        Counter<Natural> *powers;
        Counter<Natural> *max_powers = new Counter<Natural>;
        vector<pair<Natural, unsigned int> > factors;
        for (vector<Natural>::iterator i = nums.begin(); i != nums.end(); ++i) {
            // compute powers of unique prime factors of the current num
            powers = new Counter<Natural>;
            factors = primeFactorization(*i);
            for (vector<pair<Natural, unsigned int> >::iterator j = factors.begin(); j != factors.end(); ++j)
                powers->add(j->first, j->second);

            // merge with current highest powers of unique prime factors
            max_powers->merge(powers, Counter<Natural>::MERGE_FAVOR_HIGH);
            delete powers;
        }

        // return the product of prime factors raised to their highest powers
        Natural product = 1;
        for (Counter<Natural>::iterator i = max_powers->begin(); i != max_powers->end(); ++i)
            product *= power(i->first, i->second);
        delete max_powers;
        return product;
    }

    /* Returns the maximal sum of numbers from top to bottom in triangle. */
    long maxTrianglePath(vector<vector<long> > triangle) {
        const unsigned int kNumRows = triangle.size();

        // add maximum adjacent values from row above to each row
        for (unsigned int i = 1; i < kNumRows; i++) {
            for (unsigned int j = 0; j < i + 1; j++) {
                if (j != 0 && j != i)
                    // two adjacent elements above; add maximal
                    triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]);
                else if (j == 0)
                    // no adjacent element to left above; add right
                    triangle[i][j] += triangle[i - 1][j];
                else
                    // no adjacent element to right above; add left
                    triangle[i][j] += triangle[i - 1][j - 1];
            }
        }

        // return the maximum value in the last row
        vector<long> kLastRow = triangle[kNumRows - 1];
        return *max_element(kLastRow.begin(), kLastRow.end());
    }

    /* Returns a matrix of integer numbers read from input_file. */
    vector<vector<long> > numbersFromFile(const char *input_file) {
        ifstream input(input_file);
        if (!input.is_open()) {
            // failed to open the input file
            cout << "Unable to open file: " << input_file << endl;
            exit(EXIT_FAILURE);
        }

        // add each line from the input file as a row to the matrix
        string row_string;
        long entry_val;
        vector<vector<long> > matrix;
        while (getline(input, row_string)) {
            // add each token from the current line to the row vector
            vector<long> row;
            istringstream row_iss(row_string);
            while (row_iss.good()) {
                row_iss >> entry_val;
                row.push_back(entry_val);
            }

            matrix.push_back(row);
        }

        return matrix;
    }

    /* Returns a vector of the digits of the natural number n. */
    vector<short> numberToDigits(Natural n) {
        vector<short> digits;

        // append each digit of n to digits
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }

        if (digits.size() == 0)
            // if no digits have been appended, n must be 0
            digits.push_back(0);
        else
            // reverse the digits, so that they are in the correct order
            reverse(digits.begin(), digits.end());

        return digits;
    }

    /* Returns the number of permutations of k objects from a group of n. */
    BigInteger permutations(const BigInteger &n, const BigInteger &k) {
        BigInteger product("1");
        for (BigInteger i = n - k + BIG_ONE; i <= n; i++)
            product *= i;
        return product;
    }

    /* Returns the number of permutations of k objects from a group of n. */
    Natural permutations(Natural n, Natural k) {
        Natural product = 1;
        for (Natural i = n - k + 1; i <= n; i++)
            product *= i;
        return product;
    }

    /* Returns the value of m raised to the nth power. */
    Natural power(Natural m, unsigned int n) {
        // base case: m^0 = 1
        if (n == 0)
            return 1;

        // recursively compute half power
        const long long kHalfPow = power(m, n / 2);

        // compute original power
        if (n % 2 == 0)
            return kHalfPow * kHalfPow;
        else
            return m * kHalfPow * kHalfPow;
    }

    /* Returns the nth prime number. */
    Natural prime(unsigned int n) {
        computePrimes(n);
        return prime_sequence[n - 1];
    }

    /*
     * Computes the prime factorization of the natural number n. Returns a
     * vector of base-exponent pairs containing each prime factor and its power
     * in the prime factorization.
     */
    vector<pair<Natural, unsigned int> > primeFactorization(Natural n) {
        // compute potential prime factors of n
        const vector<Natural> kPrimes = primesUpTo(n);
        const unsigned int kPrimeCount = kPrimes.size();

        pair<Natural, unsigned int> factor;
        vector<pair<Natural, unsigned int> > factorization;
        for (unsigned int i = 0; i < kPrimeCount; i++) {
            // has n already been completely factored?
            if (n == 1)
                break;

            // compute power of ith prime in factorization
            factor = make_pair(kPrimes[i], 0);
            while (n % kPrimes[i] == 0) {
                n /= kPrimes[i];
                factor.second++;
            }

            // add factor to factorization if necessary
            if (factor.second > 0)
                factorization.push_back(factor);
        }

        return factorization;
    }

    /* Returns the first n prime numbers. */
    vector<Natural> primes(unsigned int n) {
        computePrimes(n);

        vector<Natural> p_list(prime_sequence.begin(),
                prime_sequence.begin() + n);
        return p_list;
    }

    /* Returns the prime numbers up to p. */
    vector<Natural> primesUpTo(Natural n) {
        computePrimesUpTo(n);

        // find the index of the last prime <= n
        unsigned int i = 0;
        const unsigned int kPrimeCount = prime_sequence.size();
        while (i < kPrimeCount && prime_sequence[i] <= n)
            i++;

        vector<Natural> p_list(prime_sequence.begin(),
                prime_sequence.begin() + i);
        return p_list;
    }

    /* Returns the sum of the decimal digits of the BigInteger n. */
    BigInteger sumDigits(const BigInteger &n) {
        // copy read-only object argument n to a writable one
        BigInteger n_copy(n);

        BigInteger sum("0");
        while (n_copy != BIG_ZERO) {
            sum += n_copy.mod10();
            n_copy /= 10;
        }
        return sum;
    }

    /* Returns the sum of the decimal digits of the natural number n. */
    Natural sumDigits(Natural n) {
        Natural sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    /* Returns the sum of the squares of the first n natural numbers. */
    Natural sumOfSquares(unsigned int n) {
        const Natural m = n;
        return (2 * m*m*m + 3 * m*m + m) / 6;
    }

    /*
     * Returns the nth triangle number, or the sum of the natural numbers up to
     * and including n.
     */
    Natural triangle(unsigned int n) {
        Natural m = n;
        return m * (m + 1) / 2;
    }
}
