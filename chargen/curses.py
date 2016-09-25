# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import npyscreen

LOGFILE = 'gui.log'

logfd = open(LOGFILE, 'w')

class Logger(object):
    def __init__(self, obj):
        if type(obj) is str:
            self.name = obj
        else:
            self.name = obj.__class__.__name__

    def write(self, msg):
        logfd.write('[%s.%s] %s\n' % (__name__, self.name, msg))
        logfd.flush()

    def __enter__(self, *args, **kwargs):
        return self.write

    def __exit__(self, *args, **kwargs):
        pass

def close_log():
    logfd.flush()
    logfd.close()

def print_log():
    with open(LOGFILE, 'rb') as stream:
        content = stream.read().decode()
    print(content)

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

class ComboBoxField(npyscreen.TitleCombo):
    def get_value(self):
        index = super(ComboBoxField, self).get_value()
        if index: return self.values[index]

class PipField(npyscreen.TitleSlider):
    def __init__(self, *args, **kwargs):
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

class Form(npyscreen.FormBaseNew):
    default_indent = 2
    indent_step = 3

    def returnFunction(self):
        self.parentApp.switchFormPrevious()

    def addReturnButton(self, name = 'Return', function = None):
        if function is None:
            function = lambda: self.parentApp.switchFormPrevious()

        self.add(EmptyLine)
        self.add(EmptyLine)
        self.add(Button, name=name, function=function)

    def addHeadline(self, name):
        self.add(HeadLine, value=name)
        self.add(EmptyLine)

    def addLink(self, name, target, indent=0, **kwargs):
        if indent > 0:
            kwargs.update({'relx': self.default_indent + (indent * self.indent_step)})

        return self.add(Link, name=name, target=target, **kwargs)

    def addField(self, name, kind = EntryField, indent=0, **kwargs):
        if indent > 0:
            kwargs.update({'relx': self.default_indent + (indent * self.indent_step)})

        return self.add(kind, name=name, **kwargs)

    def create(self):
        self.addReturnButton()

class App(npyscreen.NPSAppManaged):
    def onCleanExit(self):
        with Logger(self) as log:
            log('exiting')
        close_log()

    def print_log(self):
        print_log()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
