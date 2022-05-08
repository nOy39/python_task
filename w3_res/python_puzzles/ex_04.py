"""
We are making n stone piles! The first pile has n stones. 
If n is even, then all piles have an even number of stones. 
If n is odd, all piles have an odd number of stones. 
Each pile must more stones than the previous pile but as few as possible. 
Write a Python program to find the number of stones in each pile.
"""

n1 = 3
n2 = 17


def count_piles(n):
    return [n + 2 * i for i in range(n)]


print(count_piles(n1))
print(count_piles(n2))
