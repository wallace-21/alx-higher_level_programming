#!/usr/bin/python3

import sys

if __name__ == "__main__":

    arguments = sys.argv[:-1]

    sums = 0

    for i in arguments:

        sums += int(i)

        print(sums)
