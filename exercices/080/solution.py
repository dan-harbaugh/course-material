# -*- coding: utf-8 -*-
"""
Exercise 080
"""

alphabet1="abcdefghijklmnopqrstuvwxyz"
alphabet2="abcdefghijklmnopqrstuvwxyz"

solution=[] 

for first in alphabet1:
  for second in alphabet2:
    if first != second:
      combo=''.join(sorted(first + second))
      if combo not in solution:
        solution.insert(0,combo)

for pair in sorted(solution):
  print(pair)
