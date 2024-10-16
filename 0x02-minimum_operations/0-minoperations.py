#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method for computing the minimum number
    of operations for task Copy All and Paste
    Args:
        n: input value
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_sum = 0
    k = 2  # Start with the first prime number
    while n > 1:
        if n % k == 0:
            factor_sum += k
            n //= k  # Use integer division
        else:
            k += 1
    return factor_sum

# Example usage
result = minOperations(12)
print("Minimum operations:", result)
