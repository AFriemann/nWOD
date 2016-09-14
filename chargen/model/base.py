# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

class pip(int):
    def __init__(self, val=0):
        self.val = int(val)
        self.__check__(self.val)

    def __check__(self, value):
        if value < 0 or value > 5:
            raise ValueError("pip value must be less than 5 and greater or equal 0")

    def __add__(self, other):
        result = self.val + other
        self.__check__(result)
        return super(pip, self).__add__(other)

    def __radd__(self, other):
        result = self.val + other
        self.__check__(result)
        self.val = result

    def __rsub__(self, other):
        result = self.val - other
        self.__check__(result)
        self.val = result

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
