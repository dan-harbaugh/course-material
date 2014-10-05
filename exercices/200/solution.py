# -*- coding: utf-8 -*-
"""
Exercise 200
"""

import sys

def is_prime(num):
  if num == 1:
    return False
  if num == 2:
    return True
  if num == 3:
    return True
  counter=num-1 
  while counter > 3:
    if num % counter == 0:
      return False
    counter=counter - 1
  return True
