#!/usr/bin/python
# -*- coding: UTF-8 -*-
ANGRY_ASCII ="""
          .-''''''-.
        .' _      _ '.
       /   O      O   \\
      :                :
      |                |
      :       __       :
       \  .-"`  `"-.  /
        '.          .'
          '-......-'
     YOU SHOULDN'T BE HERE
"""

from random import randint, sample
from functools import reduce



def foo(*args):
    with open('./test.txt', 'r') as f:
        data = f.read()
        print(data)

def main():
    foo()
    # foo([('val1', 5), ('val2', 0.3), ('val3', 1)])

if __name__ == '__main__':
    main()