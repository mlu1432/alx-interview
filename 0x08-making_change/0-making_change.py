#!/usr/bin/python3
"""making changes"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount for which you need to make change.

    Returns:
        int: The fewest number of coins needed to meet the total.
        If the total cannot be met by any number of coins, return -1.
        If the total is 0 or less, return 0.
    """
    if total <= 0:
        return 0

    # Initialize dp array with 'inf', representing unreachable amounts
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case, no coins needed to make total 0

    # Update dp array for each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result for the total amount or -1 if unreachable
    return dp[total] if dp[total] != float('inf') else -1
