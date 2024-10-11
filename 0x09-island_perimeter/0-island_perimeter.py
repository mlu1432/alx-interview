#!/usr/bin/python3
"""
This module defines a function to calculate the perimeter of an island
represented by a grid.
The grid is a list of list of integers:
- 0 represents water
- 1 represents land
Each cell is connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is only one island
(or nothing).
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    Args:
        grid (list of list of int): 2D grid representing the map.

    Returns:
        int: Perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 sides to start with
                perimeter += 4
                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                # Check bottom neighbor
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                # Check right neighbor
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(island_perimeter(grid))
