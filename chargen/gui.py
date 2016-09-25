# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

from . import __version__

import logging, os, json, ruamel.yaml as pyaml

from .model.character import Character, Attributes, Skills, Virtues, Vices

from .curses import App, Logger
from .curses import Form, ActionPopup
from .curses import EmptyLine, Link, Button, EntryField, ComboBoxField, HeadLine, PipField, IntField, FilenameField

class CharForm(Form):
    def get_fields(self):
        return { k.replace('c_', ''): v for k,v in vars(self).items() if k.startswith('c_') }

    def get_char_items(self):
        return { k.replace('c_', ''): v.get_value() for k,v in self.get_fields().items() }

class CharacterAttributes(CharForm):
    def create(self):
        self.addHeadline('Mental')

        self.c_intelligence = self.addField('Intelligence', PipField, lowest=1)
        self.c_wits = self.addField('Wits', PipField, lowest=1)
        self.c_resolve = self.addField('Resolve', PipField, lowest=1)

        self.add(EmptyLine)
        self.addHeadline('Physical')

        self.c_strength = self.addField('Strength', PipField, lowest=1)
        self.c_dexterity = self.addField('Dexterity', PipField, lowest=1)
        self.c_stamina = self.addField('Resolve', PipField, lowest=1)

        self.add(EmptyLine)
        self.addHeadline('Social')

        self.c_presence = self.addField('Presence', PipField, lowest=1)
        self.c_manipulation = self.addField('Manipulation', PipField, lowest=1)
        self.c_composure = self.addField('Composure', PipField, lowest=1)

        self.addReturnButton()

class CharacterSkills(CharForm):
    def create(self):
        self.addHeadline('Mental')
        self.c_academics = self.addField('Academics', PipField)
        self.c_computer = self.addField('Computer', PipField)
        self.c_crafts = self.addField('Crafts', PipField)
        self.c_investigation = self.addField('Investigation', PipField)
        self.c_medicine = self.addField('Medicine', PipField)
        self.c_occult = self.addField('Occult', PipField)
        self.c_politics = self.addField('Politics', PipField)
        self.c_science = self.addField('Science', PipField)

        self.add(EmptyLine)
        self.addHeadline('Physical')
        self.c_athletics = self.addField('Athletics', PipField)
        self.c_brawl = self.addField('Brawl', PipField)
        self.c_drive = self.addField('Drive', PipField)
        self.c_firearms = self.addField('Firearms', PipField)
        self.c_larceny = self.addField('Larceny', PipField)
        self.c_stealth = self.addField('Stealth', PipField)
        self.c_survival = self.addField('Survival', PipField)
        self.c_weaponry = self.addField('Weaponry', PipField)

        self.add(EmptyLine)
        self.addHeadline('Social')
        self.c_animalken = self.addField('AnimalKen', PipField)
        self.c_empathy = self.addField('Empathy', PipField)
        self.c_expression = self.addField('Expression', PipField)
        self.c_intimidation = self.addField('Intimidation', PipField)
        self.c_persuasion = self.addField('Persuasion', PipField)
        self.c_socialize = self.addField('Socialize', PipField)
        self.c_streetwise = self.addField('Streetwise', PipField)
        self.c_subterfuge = self.addField('Subterfuge', PipField)

        self.addReturnButton()

class CharacterMeritsAndFlaws(CharForm):
    def create(self):
        self.addHeadline('Merits')

        self.add(EmptyLine)
        self.addHeadline('Flaws')

        self.addReturnButton()

class MainContext(CharForm):
    def create(self):
        self.c_name = self.addField('Name')
        self.c_age = self.addField('Age', IntField, value=0)
        self.c_virtue = self.addField('Virtue', ComboBoxField, values=Virtues)
        self.c_vice = self.addField('Vice', ComboBoxField, values=Vices)

        self.add(EmptyLine)

        self.addLink('Attributes', 'ATTRIBUTES')
        self.addLink('Skills', 'SKILLS')
        self.addLink('Merits & Flaws', 'MERITSANDFLAWS')

        self.addReturnButton('Load', self.load)
        self.addReturnButton('Save', self.save)
        self.addReturnButton('Exit', self.exit)

    def load(self):
        self.parentApp.switchForm('LOAD')

    def save(self):
        cname = self.parentApp.c_details.c_name.get_value().replace(' ', '-')
        self.parentApp.getForm('SAVE').fname.set_value(cname)
        self.parentApp.switchForm('SAVE')

    def exit(self):
        self.parentApp.switchForm(None)

class LoadForm(ActionPopup):
    def create(self):
        self.location = self.add(FilenameField, name='Location', value='~/')
        self.ftype = self.add(ComboBoxField, name='Filetype', values=['json', 'yaml'], value=1)

    def on_ok(self):
        abspath = os.path.expanduser(self.location.get_value())
        ftype = self.ftype.get_value()

        with Logger(self) as log:
            log('loading %s as %s' % (abspath, ftype))

        with open(abspath, 'r') as stream:
            if ftype == 'yaml':
                new_state = pyaml.safe_load(stream.read())
            elif ftype == 'json':
                new_state = json.loads(stream.read())

        self.parentApp.set_state(**new_state)

    def afterEditing(self):
        self.parentApp.switchFormPrevious()

class SaveForm(ActionPopup):
    def create(self):
        self.location = self.add(FilenameField, name='Location', value='~/')
        self.fname = self.add(EntryField, name='Filename')
        self.ftype = self.add(ComboBoxField, name='Filetype', values=['json', 'yaml'], value=1)

    def on_ok(self):
        try:
            current_state = dict(self.parentApp)
        except Excpetion as e:
            with Logger(self) as log:
                log(e)
            raise e

        location = os.path.expanduser(self.location.get_value())
        fname = self.fname.get_value()
        ftype = self.ftype.get_value()

        abspath = os.path.join(location, '%s.%s' % (fname, ftype))

        with Logger(self) as log:
            log('writing current state to %s' % abspath)

        with open(abspath, 'w') as stream:
            if ftype == 'yaml':
                stream.write(pyaml.safe_dump(current_state, default_flow_style=False))
            elif ftype == 'json':
                stream.write(json.dumps(current_state))

    def afterEditing(self):
        self.parentApp.switchFormPrevious()

class CharacterGenerator(App):
    def onStart(self):
        with Logger(self) as log:
            log('starting')

        self.c_details = self.addForm('MAIN', MainContext, name='nWOD Character Generator %s' % __version__)
        self.c_attributes = self.addForm('ATTRIBUTES', CharacterAttributes, name='Attributes')
        self.c_skills = self.addForm('SKILLS', CharacterSkills, name='Skills')
        self.c_merits_and_flaws = self.addForm('MERITSANDFLAWS', CharacterMeritsAndFlaws, name='Merits and Flaws')

        self.addForm('SAVE', SaveForm, name='Save')
        self.addForm('LOAD', LoadForm, name='Load')

    def set_state(self, **kwargs):
        self.set_form(self.c_details, **kwargs.get('details', {}))
        self.set_form(self.c_attributes, **kwargs.get('attributes', {}))
        self.set_form(self.c_skills, **kwargs.get('skills', {}))
        self.set_form(self.c_merits_and_flaws, **kwargs.get('merits_and_flaws', {}))

    def set_form(self, form, **kwargs):
        for name, proxy in form.get_fields().items():
            if name in kwargs:
                value = kwargs.get(name)
                proxy.set_value(value)

    def __iter__(self):
        yield 'details', self.c_details.get_char_items()
        yield 'attributes', self.c_attributes.get_char_items()
        yield 'skills', self.c_skills.get_char_items()

def main():
    logger = logging.getLogger(__name__)

    chargen = CharacterGenerator()
    chargen.run()

    chargen.print_log()

    try:
        print(pyaml.safe_dump(dict(chargen), default_flow_style=False))
    except Exception as e:
        logger.exception(e)
        print('Created character invalid')
        return 1

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
