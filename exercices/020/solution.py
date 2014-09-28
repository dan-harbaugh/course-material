# -*- coding: utf-8 -*-
"""
Exercise 020
"""

import sys

if len(sys.argv) != 3:
  print("usage: python3 %s OP1 OP2" % sys.argv[0] )
else:
  print(int(sys.argv[1]) - int(sys.argv[2]))
