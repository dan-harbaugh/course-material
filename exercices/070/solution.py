# -*- coding: utf-8 -*-
"""
Exercise 070
"""

alphabet="abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
  for paired in alphabet:
    if paired != char:
      print(char,end="")
      print(paired)
