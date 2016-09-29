#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import logging, os, json, ruamel.yaml as pyaml

from chargen import __version__

from chargen.gui.curses import App, Logger, ActionPopup
from chargen.gui.curses import EntryField, ComboBoxField, FilenameField

from chargen.gui.character_forms import Details, Attributes, Skills, MeritsAndFlaws

class CharacterGenerator(App):
    def __init__(self, default_dir):
        super(CharacterGenerator, self).__init__()
        self.default_dir = default_dir or '~/.local/share/nWoD/characters'

    def onStart(self):
        with Logger(self) as log:
            log('starting')

        self.details = self.addForm('MAIN', Details, name='nWOD Character Generator %s' % __version__)
        self.attributes = self.addForm('ATTRIBUTES', Attributes, name='Attributes')
        self.skills = self.addForm('SKILLS', Skills, name='Skills')
        self.merits_and_flaws = self.addForm('MERITSANDFLAWS', MeritsAndFlaws, name='Merits and Flaws')

        save_form = self.addForm('SAVE', SavePopup, name='Save')
        load_form = self.addForm('LOAD', LoadPopup, name='Load')

        save_form.location.set_value(self.default_dir)
        load_form.location.set_value(self.default_dir)

    def set_state(self, **kwargs):
        self.set_form(self.details, **kwargs.get('details', {}))
        self.set_form(self.attributes, **kwargs.get('attributes', {}))
        self.set_form(self.skills, **kwargs.get('skills', {}))
        self.set_form(self.merits_and_flaws, **kwargs.get('merits_and_flaws', {}))

    def set_form(self, form, **kwargs):
        form.set_fields(**kwargs)
        form.set_field_groups(**kwargs)

    def __iter__(self):
        yield 'details', self.details.get_values()
        yield 'attributes', self.attributes.get_values()
        yield 'skills', self.skills.get_values()
        yield 'merits & flaws', self.merits_and_flaws.get_values()

class LoadPopup(ActionPopup):
    def create(self):
        self.location = self.add(FilenameField, name='Location')
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

class SavePopup(ActionPopup):
    def create(self):
        self.location = self.add(FilenameField, name='Location')
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

        os.makedirs(location, exist_ok=True)

        with Logger(self) as log:
            log('writing current state to %s' % abspath)

        with open(abspath, 'w') as stream:
            if ftype == 'yaml':
                stream.write(pyaml.safe_dump(current_state, default_flow_style=False))
            elif ftype == 'json':
                stream.write(json.dumps(current_state))

    def afterEditing(self):
        self.parentApp.switchFormPrevious()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
