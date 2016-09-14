# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

from . import __version__

from .model.character import Character, Virtues, Vices
from .curses import Form, EmptyLine, Link, Button, App, EntryField, ComboBoxField, HeadLine

class CharacterDetails(Form):
    def create(self):

        self.addReturnButton()

class CharacterAttributes(Form):
    def create(self):
        self.addHeadline('Mental')

        self.c_intelligence = self.addField('Intelligence')
        self.c_wits = self.addField('Wits')
        self.c_resolve = self.addField('Resolve')

        self.addHeadline('Physical')
        self.addHeadline('Social')

        self.addReturnButton()

class CharacterSkills(Form):
    def create(self):
        self.addHeadline('Mental')
        self.addHeadline('Physical')
        self.addHeadline('Social')

        self.addReturnButton()

class CharacterMeritsAndFlaws(Form):
    def create(self):
        self.addHeadline('Merits')
        self.addHeadline('Flaws')

        self.addReturnButton()

class MainContext(Form):
    def create(self):
        self.addHeadline('Details')

        self.c_name = self.addField('Name')
        self.c_age = self.addField('Age')
        self.c_virtue = self.addField('Virtue', ComboBoxField, values=Virtues)
        self.c_vice = self.addField('Vice', ComboBoxField, values=Vices)

        self.c_attributes = self.addField('Attributes', kind=Link, indent=0, target='ATTRIBUTES')
        self.c_skills = self.addField('Skills', kind=Link, indent=0, target='SKILLS')
        self.c_merits_and_flaws = self.addField('Merits & Flaws', kind=Link, indent=0, target='MERITSANDFLAWS')

        self.addReturnButton('Save & Exit', self.saveAndExit)

    def saveAndExit(self):
        self.parentApp.switchForm(None)

class CharacterGenerator(App):
    character = {}

    def onStart(self):
        self.log('starting')

        self.addForm('MAIN', MainContext, name='nWOD Character Generator %s' % __version__)
        self.addForm('ATTRIBUTES', CharacterAttributes, name='Attributes')
        self.addForm('SKILLS', CharacterSkills, name='Skills')
        self.addForm('MERITSANDFLAWS', CharacterMeritsAndFlaws, name='Merits and Flaws')

    def getCharacter(self):
        return Character(**self.character)

def main():
    chargen = CharacterGenerator()
    chargen.run()

    chargen.print_log()

    try:
        print(chargen.getCharacter())
    except:
        print('Created character invalid')
        return 1

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
