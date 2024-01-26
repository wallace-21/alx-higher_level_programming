#!/usr/bin/python3

from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as output:
    out = output.read()
    print("- {}".format(out))
