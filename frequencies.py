"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if not(str(item) in frequencies):
            frequencies.update({str(item) : 1})
        else:
            oldValue = frequencies.get(str(item))
            oldValue += 1
            frequencies.update({str(item) : oldValue})

    return frequencies
