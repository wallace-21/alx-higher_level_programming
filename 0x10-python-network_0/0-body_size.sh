#!/bin/bash
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the
echo "$(curl -s "$1" | wc -c)"
