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
    academics = Attribute(pip, fallback=0)
    computer = Attribute(pip, fallback=0)
    crafts = Attribute(pip, fallback=0)
    investigation = Attribute(pip, fallback=0)
    medicine = Attribute(pip, fallback=0)
    occult = Attribute(pip, fallback=0)
    politics = Attribute(pip, fallback=0)
    science = Attribute(pip, fallback=0)

class PhysicalSkills(Model):
    athletics = Attribute(pip, fallback=0)
    brawl = Attribute(pip, fallback=0)
    drive = Attribute(pip, fallback=0)
    firearms = Attribute(pip, fallback=0)
    larceny = Attribute(pip, fallback=0)
    stealth = Attribute(pip, fallback=0)
    survival = Attribute(pip, fallback=0)
    weaponry = Attribute(pip, fallback=0)

class SocialSkills(Model):
    animalKen = Attribute(pip, fallback=0)
    empathy = Attribute(pip, fallback=0)
    expression = Attribute(pip, fallback=0)
    intimidation = Attribute(pip, fallback=0)
    persuasion = Attribute(pip, fallback=0)
    socialize = Attribute(pip, fallback=0)
    streetwise = Attribute(pip, fallback=0)
    subterfuge = Attribute(pip, fallback=0)

class Skills(Model):
    mental = Attribute(MentalSkills, fallback={})
    physical = Attribute(PhysicalSkills, fallback={})
    social = Attribute(SocialSkills, fallback={})

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
