"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4


def sublist(a, b):
    if a == b:
        return 1

    if is_sublist(a, b):
        return 2

    # Test for a is superlist of b
    if is_sublist(b, a):
        return 3

    return 4

def is_sublist(a: list, b: list) -> bool:
    for i in range(0, len(b)-len(a)+1):
        if b[i:i+len(a)] == a:
            return True

