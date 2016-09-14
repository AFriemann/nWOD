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
    Name = Attribute(str)
    Age  = Attribute(int)

    Virtue = Attribute(str)
    Vice = Attribute(str)

    Attributes = Attribute(Attributes, fallback={})
    Skills = Attribute(Skills, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
