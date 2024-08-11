#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.
    
    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

