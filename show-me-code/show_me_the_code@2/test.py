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

from enum import Enum

class EnumUserType(Enum):
    admin = 'leeing'
    common = 2
    red = 1
    green = 2
    blue = 3
    white = 3
    yellow = 8

def foo(*args):
    print(EnumUserType['red'])
    print(EnumUserType['white'])
    print('*'*10)
    print(EnumUserType(8))
    print(EnumUserType['admin'])
    print(EnumUserType('leeing'))
    print(EnumUserType['white'].name)
    print(EnumUserType['white'].value)
    for item in EnumUserType:
        print(item.name, item.value)

def main():
    foo()
    # foo([('val1', 5), ('val2', 0.3), ('val3', 1)])

if __name__ == '__main__':
    main()