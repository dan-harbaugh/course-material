# -*- coding: utf-8 -*-
"""
Exercise 102
"""

import sys

if len(sys.argv) != 4:
  print("usage: %s a_number (an_operator +-*/%%) a_number" % sys.argv[0])
  sys.exit()

operand=sys.argv[2]

if operand == "+":
  solution=int(sys.argv[1]) + int(sys.argv[3])

if operand == "-":
  solution=int(sys.argv[1]) - int(sys.argv[3])

if operand == "*":
  solution=int(sys.argv[1]) * int(sys.argv[3])

if operand == "/":
  solution=int(sys.argv[1]) / int(sys.argv[3])

print(solution)
