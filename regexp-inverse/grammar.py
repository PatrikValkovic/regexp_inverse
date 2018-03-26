#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 18:37
:Licence GNUv3
Part of regexp-inverse

"""

from string import ascii_lowercase
from grammpy import *
from grammpy_transforms import ContextFree, InverseContextFree
from pyparsers import cyk


class Symb(Nonterminal):
    def get(self):
        if len(self.to_rule.to_symbols) == 3:
            return self.to_rule.to_symbols[1].get()
        return [self.to_rule.to_symbols[0].s]

class Concat(Nonterminal):
    def get(self):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get()
        new = []
        left = self.to_rule.to_symbols[0].get()
        right = self.to_rule.to_symbols[1].get()
        for l in left:
            for r in right:
                new.append(l + r)
        return new

class Iterate(Nonterminal):
    max_count = 10
    def get(self):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get()
        v = self.to_rule.to_symbols[0].get()
        ret = []
        for s in v:  # type: str
            for cur in range(Iterate.max_count):
                t = ''
                for i in range(cur):
                    t += s
                ret.append(t)
        return ret


class Or(Nonterminal):
    def get(self):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get()
        l = self.to_rule.to_symbols[0].get()
        r = self.to_rule.to_symbols[2].get()
        return l+r


class SymbRule(Rule):
    rules = [([Symb], [ch]) for ch in ascii_lowercase]
class Bracket(Rule):
    rules = [([Symb], ['(', Or, ')'])]
class IterateRule(Rule):
    rules = [([Iterate], [Symb]), ([Iterate], [Symb, '*'])]
class ConcatRule(Rule):
    rules = [([Concat], [Iterate, Concat]), ([Concat], [Iterate])]
class OrRule(Rule):
    rules = [([Or], [Or, '+', Or]), ([Or], [Concat])]


grammar = Grammar(terminals=list(ascii_lowercase + '()*+'),
            nonterminals=[Symb, Concat, Or, Iterate],
            rules=[SymbRule, Bracket, ConcatRule, OrRule, IterateRule],
            start_symbol=Or)