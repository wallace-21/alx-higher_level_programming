#!/usr/bin/python3

from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as output:
        out = output.read()
        print("Body response:")
        print("\t- type: {}".format(type(out)))
        print("\t- content: {}".format(out))
