# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

from simple_model import Model, Attribute

from .base import pip

class MentalSkills(Model):
    Academics = Attribute(pip, fallback=0)
    Computer = Attribute(pip, fallback=0)
    Crafts = Attribute(pip, fallback=0)
    Investigation = Attribute(pip, fallback=0)
    Medicine = Attribute(pip, fallback=0)
    Occult = Attribute(pip, fallback=0)
    Politics = Attribute(pip, fallback=0)
    Science = Attribute(pip, fallback=0)

class PhysicalSkills(Model):
    Athletics = Attribute(pip, fallback=0)
    Brawl = Attribute(pip, fallback=0)
    Drive = Attribute(pip, fallback=0)
    Firearms = Attribute(pip, fallback=0)
    Larceny = Attribute(pip, fallback=0)
    Stealth = Attribute(pip, fallback=0)
    Survival = Attribute(pip, fallback=0)
    Weaponry = Attribute(pip, fallback=0)

class SocialSkills(Model):
    AnimalKen = Attribute(pip, fallback=0)
    Empathy = Attribute(pip, fallback=0)
    Expression = Attribute(pip, fallback=0)
    Intimidation = Attribute(pip, fallback=0)
    Persuasion = Attribute(pip, fallback=0)
    Socialize = Attribute(pip, fallback=0)
    Streetwise = Attribute(pip, fallback=0)
    Subterfuge = Attribute(pip, fallback=0)

class Skills(Model):
    Mental = Attribute(MentalSkills, fallback={})
    Physical = Attribute(PhysicalSkills, fallback={})
    Social = Attribute(SocialSkills, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
