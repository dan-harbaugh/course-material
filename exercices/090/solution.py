# -*- coding: utf-8 -*-
"""
Exercise 090
"""

import sys

for args in list(enumerate(sys.argv)):
  print("%d %s" % (args[0], args[1]))
