'''
Problem 63.

The 5-digit number, 16807 = 7**5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

@author: Curtis Belmonte
'''

N_MAX = 21 # default: 21

###############################################################################

ans_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for n in range(2, N_MAX + 1):
    B = 2
    bn = B**n
    bn_digits = len(str(bn))
    while bn_digits <= n:
        if bn_digits == n:
            ans_set.add(bn)
        B += 1
        bn = B**n
        bn_digits = len(str(bn))
print(len(ans_set))