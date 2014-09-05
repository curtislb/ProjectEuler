"""problem_033.py

Problem 33: Digit canceling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are non-trivial examples of this type of fraction, less than one in
value, and containing D digits in the numerator and denominator.

If the product of these fractions is given in its lowest common terms, find the
value of the denominator.

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

D = 2 # default: 2

# SOLUTION ####################################################################

if __name__ == '__main__':
    # compute minimum and maximum D-digit numbers
    MIN_VALUE = 10**(D - 1)
    MAX_VALUE = 10**D - 1
    
    # search for all fractions that satisfy the problem conditions
    product_numer = 1
    product_denom = 1
    for numerator in range(MIN_VALUE, MAX_VALUE):
        for denominator in range(numerator + 1, MAX_VALUE + 1):
            # compute the properly reduced numerator and denominator
            gcd = common.gcd(numerator, denominator)
            reduced_numer = numerator // gcd
            reduced_denom = denominator // gcd
            
            # cancel all cancelable digits of numerator and denominator
            numer_str = str(numerator)
            denom_str = str(denominator)
            for i in range(D):
                # does digit canceled fraction equal reduced fraction?
                match_found = False
                
                for j in range(D):
                    # check if digits can be canceled non-trivially
                    if (numer_str[i] == denom_str[j] and numer_str[i] != '0'):
                        # cancel matching digits in numerator and denominator
                        canceled_numer = int(numer_str[:i] + numer_str[i + 1:])
                        canceled_denom = int(denom_str[:j] + denom_str[j + 1:])
                        
                        # compute reduced value of digit canceled fraction
                        gcd = common.gcd(canceled_numer, canceled_denom)
                        reduced_canceled_numer = canceled_numer // gcd
                        reduced_canceled_denom = canceled_denom // gcd
                        
                        # compare digit canceled fraction to reduced fraction
                        if (reduced_canceled_numer == reduced_numer
                            and reduced_canceled_denom == reduced_denom):
                            # fractions match; add fraction to product
                            product_numer *= reduced_numer
                            product_denom *= reduced_denom
                            match_found = True
                            break
                
                # stop search if digit canceled match has already been found
                if match_found:
                    break
    
    # print the reduced denominator of product
    print(product_denom // common.gcd(product_numer, product_denom))
