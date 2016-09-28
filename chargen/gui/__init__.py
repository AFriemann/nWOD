# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import logging, os, json, ruamel.yaml as pyaml

from chargen import __version__

from chargen.model.character import Character, Attributes, Skills, Virtues, Vices

from chargen.gui.curses import App, Logger
from chargen.gui.curses import Form, ActionPopup
from chargen.gui.curses import Link, Button, EntryField, ComboBoxField, HeadLine, PipField, IntField, FilenameField

class CharacterAttributes(Form):
    def create(self):
        self.addFieldGroup(name='Mental',
            intelligence = { 'name': 'Intelligence', 'kind': PipField, 'lowest': 1 },
            wits         = { 'name': 'Wits', 'kind': PipField, 'lowest': 1 },
            resolve      = { 'name': 'Resolve', 'kind': PipField, 'lowest': 1 },
        )

        self.addEmptyLine()
        self.addFieldGroup('Physical',
            strength  = { 'name': 'Strength', 'kind': PipField, 'lowest': 1 },
            dexterity = { 'name': 'Dexterity', 'kind': PipField, 'lowest': 1 },
            stamina   = { 'name': 'Resolve', 'kind': PipField, 'lowest': 1 },
        )

        self.addEmptyLine()
        self.addFieldGroup('Social',
            presence     = { 'name': 'Presence', 'kind': PipField, 'lowest': 1 },
            manipulation = { 'name': 'Manipulation', 'kind': PipField, 'lowest': 1 },
            composure    = { 'name': 'Composure', 'kind': PipField, 'lowest': 1 },
        )

        self.addReturnButton()

class CharacterSkills(Form):
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

class CharacterMeritsAndFlaws(Form):
    def create(self):
        self.addHeadline('Merits')

        self.addEmptyLine()
        self.addHeadline('Flaws')

        self.addReturnButton()

class MainContext(Form):
    def create(self):
        self.load_menu = self.add_menu(name='File', shortcut="^F")
        self.load_menu.addItem(text='Save', onSelect=self.save, shortcut="^S")
        self.load_menu.addItem(text='Load', onSelect=self.load, shortcut="^L")

        self.field_name   = self.addField('Name')
        self.field_age    = self.addField('Age', IntField, value=0)
        self.field_virtue = self.addField('Virtue', ComboBoxField, values=Virtues)
        self.field_vice   = self.addField('Vice', ComboBoxField, values=Vices)

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
        except Exception as e:
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

        self.details = self.addForm('MAIN', MainContext, name='nWOD Character Generator %s' % __version__)
        self.attributes = self.addForm('ATTRIBUTES', CharacterAttributes, name='Attributes')
        self.skills = self.addForm('SKILLS', CharacterSkills, name='Skills')
        self.merits_and_flaws = self.addForm('MERITSANDFLAWS', CharacterMeritsAndFlaws, name='Merits and Flaws')

        self.addForm('SAVE', SaveForm, name='Save')
        self.addForm('LOAD', LoadForm, name='Load')

    def set_state(self, **kwargs):
        self.set_form(self.details, **kwargs.get('details', {}))
        self.set_form(self.attributes, **kwargs.get('attributes', {}))
        self.set_form(self.skills, **kwargs.get('skills', {}))
        self.set_form(self.merits_and_flaws, **kwargs.get('merits_and_flaws', {}))

    def set_form(self, form, **kwargs):
        form.set_fields(**kwargs)
        form.set_field_groups(**kwargs)

    def __iter__(self):
        yield 'details', self.details.get_items()
        yield 'attributes', self.attributes.get_items()
        yield 'skills', self.skills.get_items()
        yield 'merits & flaws', self.merits_and_flaws.get_items()

def run():
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
