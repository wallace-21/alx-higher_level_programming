#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arglength = len(sys.argv)

    if arglength == 1:

        print("{} arguments.".format(arglength - 1))

    elif arglength == 2:

        print("{} argument:".format(arglength - 1))

    else:
        print("{} arguments:".format(arglength - 1))

    for i in range(1, arglength):

        print("{}: {}".format(i, sys.argv[i]))
