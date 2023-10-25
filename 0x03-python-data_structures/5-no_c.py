#!/usr/bin/python3
def no_c(my_string):

    result = ""

    for elements in my_string:

        if elements != 'c' and elements != 'C':

            result += elements

    return (result)
