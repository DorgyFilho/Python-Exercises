#099 - Write a Python program to generate all permutations of a list in Python.
# In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some 
# sequence or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. 
# These differ from combinations, which are selections of some members of a set where order is disregarded.
# In the following image each of the six rows is a different permutation of three distinct balls.

import itertools
print(list(itertools.permutations([1,2])))
