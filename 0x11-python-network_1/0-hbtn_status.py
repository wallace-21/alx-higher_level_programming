#!/usr/bin/python3

"""import url library"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as output:
        out = output.read()
        print("Body response:")
        print("\t- type: {}".format(type(out)))
        print("\t- content: {}".format(out))
        print("\t- utf8 content: {}".format(out.decode('utf-8')))
