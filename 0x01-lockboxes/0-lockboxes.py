#!/usr/bin/python3
"""
This module contains a function `canUnlockAll` that determines if all the boxes in a list
can be unlocked starting from the first box (boxes[0]).
Returns:
- bool: True if all boxes can be opened, otherwise False.
"""
def canUnlockAll(boxes):
    opened_boxes = set()
    keys = [0]

    while keys:
        current_key = keys.pop()

        if current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys.extend(boxes[current_key])

    return len(opened_boxes) == len(boxes)
