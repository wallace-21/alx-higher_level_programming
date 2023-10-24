#!/usr/bin/python3

for i in range(9):
    for a in range(i + 1, 10):
        if i * 10 + a < 89:
            print("{:d}{:d}".format(i, a), end=", ")
print("{:d}".format(99))
