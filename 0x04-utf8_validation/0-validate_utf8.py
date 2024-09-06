#!/usr/bin/python3
"""
This script contains a function to validate UTF-8 encoding.

The validUTF8 function determines if a given dataset (list of integers)
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Function that determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    bytes_to_process = 0

    for byte in data:
        # Only keep the last 8 bits (1 byte)
        byte = byte & 0xFF

        if bytes_to_process == 0:
            # Determine how many bytes are in this UTF-8 character
            if (byte >> 5) == 0b110:
                bytes_to_process = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_process = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_process = 3
            elif (byte >> 7):
                return False  # Invalid 1-byte character
        else:
            # Check that it's a continuation byte (starts with '10')
            if (byte >> 6) != 0b10:
                return False
            bytes_to_process -= 1

    # If bytes_to_process is not 0, it means there are incomplete characters
    return bytes_to_process == 0
