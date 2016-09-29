# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

from chargen.gui.curses import FormWithMenus, SimpleForm, Logger
from chargen.gui.curses import PipField, IntField, ComboBoxField

Virtues = [ 'Charity', 'Faith', 'Fortitude', 'Hope', 'Justice', 'Prudence', 'Temperance' ]
Vices   = [ 'Envy', 'Gluttony', 'Greed', 'Lust', 'Pride', 'Sloth', 'Wrath' ]

class Details(FormWithMenus):
    def create(self):
        self.load_menu = self.add_menu(name='File', shortcut="^F")
        self.load_menu.addItem(text='Save', onSelect=self.save, shortcut="^S")
        self.load_menu.addItem(text='Load', onSelect=self.load, shortcut="^L")

        self.field_name     = self.addField('Name')
        self.field_campaign = self.addField('Campaign')
        self.field_age      = self.addField('Age', IntField, value=0)
        self.field_virtue   = self.addField('Virtue', ComboBoxField, values=Virtues)
        self.field_vice     = self.addField('Vice', ComboBoxField, values=Vices)

        self.addEmptyLine()

        self.addLink('Attributes', 'ATTRIBUTES')
        self.addLink('Skills', 'SKILLS')
        self.addLink('Merits & Flaws', 'MERITSANDFLAWS')

        self.addEmptyLine()

        self.addReturnButton('Exit', self.exit)

    def load(self):
        self.parentApp.switchForm('LOAD')

    def save(self):
        cname = self.parentApp.details.get_field('name').get_value().replace(' ', '-')
        self.parentApp.getForm('SAVE').fname.set_value(cname)

        self.parentApp.switchForm('SAVE')

    def exit(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

class Attributes(SimpleForm):
    def create(self):
        self.addFieldGroup(name='Mental',
            intelligence = { 'name': 'Intelligence', 'kind': PipField, 'lowest': 1 },
            wits         = { 'name': 'Wits', 'kind': PipField, 'lowest': 1 },
            resolve      = { 'name': 'Resolve', 'kind': PipField, 'lowest': 1 },
            _callback = self.update_pips,
        )

        self.addEmptyLine()
        self.addFieldGroup('Physical',
            strength  = { 'name': 'Strength', 'kind': PipField, 'lowest': 1 },
            dexterity = { 'name': 'Dexterity', 'kind': PipField, 'lowest': 1 },
            stamina   = { 'name': 'Resolve', 'kind': PipField, 'lowest': 1 },
            _callback = self.update_pips,
        )

        self.addEmptyLine()
        self.addFieldGroup('Social',
            presence     = { 'name': 'Presence', 'kind': PipField, 'lowest': 1 },
            manipulation = { 'name': 'Manipulation', 'kind': PipField, 'lowest': 1 },
            composure    = { 'name': 'Composure', 'kind': PipField, 'lowest': 1 },
            _callback = self.update_pips,
        )

        self.mps = self.calculate_mps()

        self.addEmptyLine()
        self.addEmptyLine()
        self.mps_pips = self.addField('M/P/S', editable=False, value=self.mps)

        self.addReturnButton()

    def calculate_mps(self):
        pips = {}
        for group, items in self.get_field_groups():
            pips[group] = self.accumulate_pips(items) - 3 # default value is 1
        return '{mental}/{physical}/{social}'.format(**pips)

    def accumulate_pips(self, pip_fields):
        return sum([ proxy.get_value() for proxy in pip_fields.values() ])

    def update_pips(self, *args, **kwargs):
        old_mps = self.mps
        self.mps = self.calculate_mps()

        if old_mps != self.mps:
            self.mps_pips.set_value(self.mps)
            self.mps_pips.update()

class Skills(SimpleForm):
    def create(self):
        self.addFieldGroup('Mental',
            academics     = { 'name': 'Academics', 'kind': PipField },
            computer      = { 'name': 'Computer', 'kind': PipField },
            crafts        = { 'name': 'Crafts', 'kind': PipField },
            investigation = { 'name': 'Investigation', 'kind': PipField },
            medicine      = { 'name': 'Medicine', 'kind': PipField },
            occult        = { 'name': 'Occult', 'kind': PipField },
            politics      = { 'name': 'Politics', 'kind': PipField },
            science       = { 'name': 'Science', 'kind': PipField },
        )

        self.addEmptyLine()
        self.addFieldGroup('Physical',
            athletics = { 'name': 'Athletics', 'kind': PipField },
            brawl     = { 'name': 'Brawl', 'kind': PipField },
            drive     = { 'name': 'Drive', 'kind': PipField },
            firearms  = { 'name': 'Firearms', 'kind': PipField },
            larceny   = { 'name': 'Larceny', 'kind': PipField },
            stealth   = { 'name': 'Stealth', 'kind': PipField },
            survival  = { 'name': 'Survival', 'kind': PipField },
            weaponry  = { 'name': 'Weaponry', 'kind': PipField },
        )

        self.addEmptyLine()
        self.addFieldGroup('Social',
            animalken    = { 'name': 'Animal Ken', 'kind': PipField },
            empathy      = { 'name': 'Empathy', 'kind': PipField },
            expression   = { 'name': 'Expression', 'kind': PipField },
            intimidation = { 'name': 'Intimidation', 'kind': PipField },
            persuasion   = { 'name': 'Persuasion', 'kind': PipField },
            socialize    = { 'name': 'Socialize', 'kind': PipField },
            streetwise   = { 'name': 'Streetwise', 'kind': PipField },
            subterfuge   = { 'name': 'Subterfuge', 'kind': PipField },
        )

        self.addReturnButton()

class MeritsAndFlaws(SimpleForm):
    def create(self):
        self.addHeadline('Merits')

        self.addEmptyLine()
        self.addHeadline('Flaws')

        self.addReturnButton()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
