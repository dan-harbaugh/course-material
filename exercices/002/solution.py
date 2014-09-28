# -*- coding: utf-8 -*-
"""
Exercise 002
"""
def reverse_string(string):
  length = len(string)
  reverse_string=''
  while length>0:
    character=string[length - 1:length]
    if character in 'aeiou':
      character = character.upper()
    reverse_string=reverse_string + character
    length = length - 1
  return reverse_string

print (reverse_string("abcdefghijklmnopqrstuvwxyz"))
