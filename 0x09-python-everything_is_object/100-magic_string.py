#!/usr/bin/python3
def magic_string():
    magic_string.keep_count = getattr(magic_string, 'keep_count', 0) + 1
    return ("BestSchool" + ", BestSchool" * (magic_string.keep_count - 1))
