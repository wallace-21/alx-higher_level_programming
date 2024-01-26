#!/usr/bin/python3

from urllib import request
import sys

put = sys.argv[1]
with request.urlopen(put) as output:
    request_id = output.headers['X-Request-Id']
    print(request_id)
