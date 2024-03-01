#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if list_of_integers:
        lf = 0
        r = len(list_of_integers) - 1
        while lf < r:
            m = (lf + r) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                r = m
            else:
                lf = m + 1
        return list_of_integers[lf]
