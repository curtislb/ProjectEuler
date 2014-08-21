'''
Problem 22.

Using FILE, a large text file containing many first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

@author: Curtis Belmonte
'''

FILE = 'input/022.txt'

###############################################################################

from heapq import heapify, heappop

from common import alpha_num_uc, list_from_ssv

file = open(FILE, 'r')
name_heap = list_from_ssv(file.read())
heapify(name_heap)

total = 0
for n in range(1, len(name_heap) + 1):
    name = (heappop(name_heap)).strip()
    total += n * sum([alpha_num_uc(letter) for letter in name])
print(total)