#!/usr/bin/python3
"""
This module contains a function `canUnlockAll` that determines if all the boxes in a list
can be unlocked starting from the first box (boxes[0]).

Parameters:
- boxes (list of lists): A list where each element is a list of integers representing the keys found in each box.

Returns:
- bool: True if all boxes can be opened, otherwise False.
"""
def canUnlockAll(boxes):
    if not boxes:
        return False

    opened_boxes = set([0])
    keys = list(boxes[0])

    while keys:
        current_key = keys.pop()

 
        if current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys.extend(boxes[current_key])


    return len(opened_boxes) == len(boxes)