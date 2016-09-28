# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import npyscreen

from chargen.gui.curses.logger import Logger

class Link(npyscreen.ButtonPress):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'name': '%s ->' % kwargs.get('name'),
            'color': 'WHITE_BLACK',
            'relx': 0,
        })
        super(Link, self).__init__(*args, **kwargs)
        self.target = kwargs.get('target')

    def whenPressed(self):
        self.parent.parentApp.switchForm(self.target)

class Button(npyscreen.ButtonPress):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self.function = kwargs.get('function')

    def whenPressed(self):
        self.function()

class EmptyLine(npyscreen.FixedText):
    def __init__(self, *args, **kwargs):
        super(EmptyLine, self).__init__(*args, value='\n', editable=False, **kwargs)

class HeadLine(npyscreen.FixedText):
    def __init__(self, *args, **kwargs):
        kwargs.update({'relx': 5})
        super(HeadLine, self).__init__(*args, editable=False, **kwargs)

class EntryField(npyscreen.TitleText):
    pass

class IntField(npyscreen.TitleText):
    def __init__(self, *args, **kwargs):
        kwargs['value'] = str(kwargs.get('value', 0))
        super(IntField, self).__init__(*args, **kwargs)

    def get_value(self):
        return int(super(IntField, self).get_value())

    def set_value(self, value):
        super(IntField, self).set_value(str(value))

class ComboBoxField(npyscreen.TitleCombo):
    def get_value(self):
        index = super(ComboBoxField, self).get_value()
        if index: return self.values[index]

class PipField(npyscreen.TitleSlider):
    def __init__(self, *args, **kwargs):
        if 'lowest' not in kwargs: kwargs['lowest'] = 0
        if 'value' not in kwargs: kwargs['value'] = kwargs['lowest']
        super(PipField, self).__init__(
            *args,
            out_of=5, field_width=25,
            **kwargs)

    def get_value(self):
        return int(super(PipField, self).get_value())

class FilenameField(npyscreen.TitleFilename):
    pass

class Popup(npyscreen.Popup):
    pass

class ActionPopup(npyscreen.ActionPopup):
    pass

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
