#!/usr/bin/python3

"""import url library and system module"""
from urllib import request
from urllib import parse
import sys

url = sys.argv[1]
email = sys.argv[2]
my_data = {
    "email": email
}

if __name__ == "__main__":
    encode_email = parse.urlencode(my_data).encode('utf-8')

    req = request.Request(url, data=encode_email, method="POST")

    with request.urlopen(req) as output:
            out = output.read().decode('utf-8')
            print(out)
