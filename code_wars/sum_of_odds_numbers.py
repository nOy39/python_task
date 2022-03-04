"""
Given the triangle of consecutive odd numbers:

1->              1
2->           3     5
3->        7     9    11
4->    13    15    17    19
5->  21    23    25    27    29
6-> 31  33  35  37  39  41
7-> 43  45  47  49  51  53  55
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1)
"""


def row_sum_odd_numbers(n):
    return n ** 3


print(row_sum_odd_numbers(13))
