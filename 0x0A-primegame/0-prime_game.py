#!/usr/bin/python3
"""
Prime Game module.
"""

def isWinner(x, nums):
    """
    Determines the winner of each game.
    
    Args:
        x: number of rounds
        nums: array of n values for each round
    
    Returns:
        Name of the player that won the most rounds ("Maria" or "Ben")
        or None if there is no clear winner.
    """
    if x < 1 or not nums:
        return None

    # Determine the maximum value of n we need to consider
    max_n = max(nums)

    # Step 1: Use the Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Step 2: Precompute the number of primes up to each number up to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:

        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
