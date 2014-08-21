'''
Problem 76.

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can N be written as a sum of at least two positive
integers?

@author: Curtis Belmonte
'''

N = 100 # default: 100

###############################################################################

from common import sum_combos

print(sum_combos(N, list(range(1, N))))
