#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 26.03.2018 19:38
:Licence GNUv3
Part of regexp-inverse

"""


from unittest import TestCase, main
from regexp_inverse import generate


class HashContainerSimpleTest(TestCase):
    def test_concatenation(self):
        res = generate('ab')
        self.assertEqual(res, ['ab'])

    def test_or(self):
        res = generate('a+b')
        self.assertIn('a', res)
        self.assertIn('b', res)

    def test_iteration(self):
        res = generate('a*', iterations=3, fill=None)
        self.assertIn('', res)
        self.assertIn('a', res)
        self.assertIn('aa', res)
        self.assertIn('aaa', res)

    def test_iterationWithFill(self):
        res = generate('a*', iterations=3, fill='...')
        self.assertIn('', res)
        self.assertIn('a', res)
        self.assertIn('aa', res)
        self.assertIn('aaa', res)
        self.assertIn('aa...aa', res)

    def test_combined(self):
        res = generate('ab*(def+xy*z)', iterations=3, fill='...')
        self.assertIn('adef', res)
        self.assertIn('abdef', res)
        self.assertIn('abbdef', res)
        self.assertIn('abbbdef', res)
        self.assertIn('abb...bbdef', res)
        self.assertIn('axz', res)
        self.assertIn('abxz', res)
        self.assertIn('abbxz', res)
        self.assertIn('abbbxz', res)
        self.assertIn('abb...bbxz', res)
        self.assertIn('axyz', res)
        self.assertIn('abxyz', res)
        self.assertIn('abbxyz', res)
        self.assertIn('abbbxyz', res)
        self.assertIn('abb...bbxyz', res)
        self.assertIn('axyyz', res)
        self.assertIn('abxyyz', res)
        self.assertIn('abbxyyz', res)
        self.assertIn('abbbxyyz', res)
        self.assertIn('abb...bbxyyz', res)
        self.assertIn('axyyyz', res)
        self.assertIn('abxyyyz', res)
        self.assertIn('abbxyyyz', res)
        self.assertIn('abbbxyyyz', res)
        self.assertIn('abb...bbxyyyz', res)
        self.assertIn('axyy...yyz', res)
        self.assertIn('abxyy...yyz', res)
        self.assertIn('abbxyy...yyz', res)
        self.assertIn('abbbxyy...yyz', res)
        self.assertIn('abb...bbxyy...yyz', res)


if __name__ == '__main__':
    main()
