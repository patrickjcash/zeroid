import math
import itertools

# recursive test for Zeroid-ness. takes a list of integers as input
def is_zeroid(x):
    if len(x) == 1:
        return x[0] == 0
    elif len(x) == 2:
        return is_zeroid(int_to_list(abs(x[0] - x[1]))) \
            or is_zeroid(int_to_list(x[0] + x[1]))      \
            or is_zeroid(int_to_list(x[0] * x[1]))
    elif len(x) > 2:
        t = False
        for z in itertools.permutations(x):
            y = list(z)
            t = t or is_zeroid(int_to_list(abs(y[0] - y[1])) + y[2:]) \
                  or is_zeroid(int_to_list(y[0] + y[1]) + y[2:])      \
                  or is_zeroid(int_to_list(y[0] * y[1]) + y[2:])
        return t

# convert an integer to a list of integer digits
def int_to_list(num):
    return [int(x) for x in str(num)]

# test numbers from 0 to x
for i in range(0,100):
    print(i,"...",is_zeroid(int_to_list(i)))