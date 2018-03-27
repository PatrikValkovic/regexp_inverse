#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 18:42
:Licence GNUv3
Part of regexp-inverse

"""

from optparse import OptionParser

cmd_parser = OptionParser('usage: %prog [options] regular-expression')
cmd_parser.add_option('-i', '--iterations',
                      help='max count of iterations',
                      type='int',
                      default=8)
cmd_parser.add_option('-f', '--fill',
                      help='fill symbol in iterations',
                      type='string',
                      default=None)
