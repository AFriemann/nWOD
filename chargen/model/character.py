# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

from simple_model import Model, Attribute

from .attributes import Attributes
from .skills import Skills

Virtues = [ 'Charity', 'Faith', 'Fortitude', 'Hope', 'Justice', 'Prudence', 'Temperance' ]
Vices   = [ 'Envy', 'Gluttony', 'Greed', 'Lust', 'Pride', 'Sloth', 'Wrath' ]

class Character(Model):
    name = Attribute(str)
    age  = Attribute(int)

    virtue = Attribute(str)
    vice = Attribute(str)

    attributes = Attribute(Attributes, fallback={})
    skills = Attribute(Skills, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
