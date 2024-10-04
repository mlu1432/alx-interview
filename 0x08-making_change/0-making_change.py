#!/usr/bin/python3
"""
Coin Change Algorithm using a Greedy Approach.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of available coin values.
        total (int): The target amount of change.

    Returns:
        int: The fewest number of coins needed to reach the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to use the largest denomination first
    coins.sort(reverse=True)

    ncoins = 0  # Counter for number of coins used
    cpy_total = total

    for coin in coins:
        # Use as many of the current coin as possible
        while cpy_total >= coin:
            cpy_total -= coin
            ncoins += 1

        # If we have made the exact total, break
        if cpy_total == 0:
            break

    # If there's any remaining amount, return -1 (change not possible)
    return -1 if cpy_total > 0 else ncoins
