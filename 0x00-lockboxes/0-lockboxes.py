#!/usr/bin/python3


def canUnlockAll(boxes):
    """lockboxes"""
    list_comparation = []

    for box in range(len(boxes)):
        for key in boxes[box]:
            if key != box and key < len(boxes) and \
               key != 0 and key not in list_comparation:
                list_comparation.append(key)

    return True if len(list_comparation) == (len(boxes) - 1) else False