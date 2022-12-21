#!/usr/bin/env python3
import re

string = """Hello my number is 123456789
            My friends number is 987654321"""
regex = '\d+'

match = re.findall(regex,string)

print(match)

another_regex = "123"

another_match = re.findall(another_regex,string)

print(another_match)
