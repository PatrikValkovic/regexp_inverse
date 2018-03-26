#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 18:50
:Licence GNUv3
Part of regexp-inverse

"""

from grammpy_transforms import *
from pyparsers import cyk

from .reg_grammar import grammar


def generate(expr, max_length=1024, iterations=8, fill=None):
    ContextFree.remove_useless_symbols(grammar, transform_grammar=True)
    ContextFree.remove_rules_with_epsilon(grammar, transform_grammar=True)
    ContextFree.remove_unit_rules(grammar, transform_grammar=True)
    ContextFree.remove_useless_symbols(grammar, transform_grammar=True)
    ContextFree.transform_to_chomsky_normal_form(grammar, transform_grammar=True)

    parsed = cyk(grammar, expr)

    parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
    parsed = InverseContextFree.unit_rules_restore(parsed)
    parsed = InverseContextFree.epsilon_rules_restore(parsed)

    return parsed.get(max_length, iterations, fill)
