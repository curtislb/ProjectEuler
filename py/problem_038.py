'''
Problem 38.

Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

@author: Curtis Belmonte
'''
from common import INF, is_permutation, PAN_STR, str_permutations

max_num = -INF
for digits in range(1, 5):
    for perm in str_permutations(PAN_STR, digits):
        base_num = int(perm)
        
        n = 2
        prod_str = str(base_num) + str(base_num * 2)
        while len(prod_str) < 9:
            n += 1
            prod_str += str(base_num * n)
        if len(prod_str) > 9:
            continue
        if is_permutation(prod_str, PAN_STR):
            num = int(prod_str)
            if num > max_num:
                max_num = num
print(max_num)