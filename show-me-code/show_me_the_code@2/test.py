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
def foo(*args):
    print(args)
    values = zip(*args)
    print(values)
    for item in values:
        print(item)

def main():
    foo(1,2,3)
    # foo([('val1', 5), ('val2', 0.3), ('val3', 1)])

if __name__ == '__main__':
    main()