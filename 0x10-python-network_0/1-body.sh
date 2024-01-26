#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the re
output=$(curl -s -w "%{http_code}" $1); echo "$out"
