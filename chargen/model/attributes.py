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
    Intelligence = Attribute(pip, fallback=1)
    Resolve = Attribute(pip, fallback=1)
    Wits = Attribute(pip, fallback=1)

class PhysicalAttributes(AttributeCategory):
    Dexterity = Attribute(pip, fallback=1)
    Stamina = Attribute(pip, fallback=1)
    Strength = Attribute(pip, fallback=1)

class SocialAttributes(AttributeCategory):
    Composure = Attribute(pip, fallback=1)
    Manipulation = Attribute(pip, fallback=1)
    Presence = Attribute(pip, fallback=1)

class Attributes(Model):
    Mental = Attribute(MentalAttributes, fallback={})
    Physical = Attribute(PhysicalAttributes, fallback={})
    Social = Attribute(SocialAttributes, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
