# -*- coding: utf-8 -*-
"""
Exercise 201
"""

import sys

def is_alpha(input):
  LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for character in input:
    if character.upper() not in LETTERS:
      return False
  return True

print(is_alpha("prime4"))
