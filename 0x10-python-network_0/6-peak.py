#!/usr/bin/python3

"""function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):

    if not list_of_integers:
        return None

    n = len(list_of_integers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_integers[j] < list_of_integers[j + 1]:
                list_of_integers[j], list_of_integers[j + 1] = list_of_integers[j + 1], list_of_integers[j]
    return list_of_integers[0]
