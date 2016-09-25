# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import sys

from simple_model import Model, Attribute

from .base import pip

class AttributeCategory(Model):
    @classmethod
    def __from_input__(cls, points):
        return cls()

class MentalAttributes(AttributeCategory):
    intelligence = Attribute(pip, fallback=1)
    resolve = Attribute(pip, fallback=1)
    wits = Attribute(pip, fallback=1)

class PhysicalAttributes(AttributeCategory):
    dexterity = Attribute(pip, fallback=1)
    stamina = Attribute(pip, fallback=1)
    strength = Attribute(pip, fallback=1)

class SocialAttributes(AttributeCategory):
    composure = Attribute(pip, fallback=1)
    manipulation = Attribute(pip, fallback=1)
    presence = Attribute(pip, fallback=1)

class Attributes(Model):
    mental = Attribute(MentalAttributes, fallback={})
    physical = Attribute(PhysicalAttributes, fallback={})
    social = Attribute(SocialAttributes, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
