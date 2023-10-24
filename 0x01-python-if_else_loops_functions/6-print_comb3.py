#!/usr/bin/python3

for i in range(9):
    for a in range(i + 1, 10):
        if i * 10 + a < 89:
            print("{:}{:}".format(i, a), end=", ")
print("{:}".format(89))
