#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 19:17
:Licence GNUv3
Part of regexp-inverse

"""

from regexp_inverse import *

if __name__ == '__main__':
    (options, args) = cmd_parser.parse_args()
    if len(args) != 1:
        print('Invalid count of arguments')
        exit(1)
    for sentence in generate(args[0], options.max_length, options.iterations, options.fill):
        print(sentence)
    exit(0)
