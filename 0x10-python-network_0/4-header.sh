#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the
curl -H "X-School-User-Id: 98" -X GET "$1"
