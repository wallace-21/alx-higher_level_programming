#!/usr/bin/python3

"""import url library"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as output:
        out = output.read()
        print("Body response:")
        print("    - type: {}".format(type(out)))
        print("    - content: {}".format(out))
