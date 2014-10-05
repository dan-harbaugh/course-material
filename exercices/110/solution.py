# -*- coding: utf-8 -*-
"""
Exercise 102
"""

import sys

if len(sys.argv) != 4:
  print("usage: %s a_number (an_operator +-*/%%) a_number" % sys.argv[0])

operand=sys.argv[2]

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

if operand == "+":
  solution=expr(sys.argv[1] + sys.argv[3])

#print(sys.argv[2] sys.argv[3] sys.argv[4])

print(solution)
