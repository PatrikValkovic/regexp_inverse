#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 18:37
:Licence GNUv3
Part of regexp-inverse

"""

from string import ascii_lowercase
from grammpy import *


class Symb(Nonterminal):
    def get(self, i, f):
        if len(self.to_rule.to_symbols) == 3:
            return self.to_rule.to_symbols[1].get(i, f)
        return [self.to_rule.to_symbols[0].s]

class Concat(Nonterminal):
    def get(self, i, f):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get(i, f)
        new = []
        left = self.to_rule.to_symbols[0].get(i, f)
        right = self.to_rule.to_symbols[1].get(i, f)
        for l in left:
            for r in right:
                new.append(l + r)
        return new

class Iterate(Nonterminal):
    def get(self, i, f):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get(i, f)
        v = self.to_rule.to_symbols[0].get(i, f)
        ret = []
        for s in v:  # type: str
            for cur in range(i+1):
                t = ''
                for j in range(cur):
                    t += s
                ret.append(t)
            if f is not None:
                t = ''
                for j in range(i-1):
                    t += s
                t += f
                for j in range(i-1):
                    t += s
                ret.append(t)
        return ret


class Or(Nonterminal):
    def get(self, i, f):
        if len(self.to_rule.to_symbols) == 1:
            return self.to_rule.to_symbols[0].get(i, f)
        l = self.to_rule.to_symbols[0].get(i, f)
        r = self.to_rule.to_symbols[2].get(i, f)
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