# -*- coding: utf-8 -*-
"""
Exercise 202
"""

import sys

def starts_with(input, value):
  if len(value) > len(input):
    return False
  length=len(value)
  counter=length-1
  while counter > 0:
    if value[counter] != input[counter]:
      return False
    counter=counter-1
  return True
