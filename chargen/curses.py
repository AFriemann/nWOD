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

def close_log():
    logfd.flush()
    logfd.close()

def print_log():
    with open(LOGFILE, 'rb') as stream:
        content = stream.read().decode()
    print(content)

def log_function(obj):
    clsname = obj.__class__.__name__
    def log(msg):
        logfd.write('[%s.%s] %s\n' % (__name__, clsname, msg))
        logfd.flush()
    return log

class Link(npyscreen.ButtonPress):
    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)
        self.log = log_function(self)

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
        super(EmptyLine, self).__init__(*args, editable=False, **kwargs)
        self.value = '\n'

class HeadLine(npyscreen.FixedText):
    def __init__(self, *args, **kwargs):
        super(HeadLine, self).__init__(*args, editable=False, **kwargs)
        #self.value = '-------%s-------' % self.value

class EntryField(npyscreen.TitleText):
    pass

class ComboBoxField(npyscreen.TitleCombo):
    pass

class Form(npyscreen.FormBaseNew):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.log = log_function(self)

    def returnFunction(self):
        self.parentApp.switchFormPrevious()

    def addReturnButton(self, name = 'Return', function = None):
        if function is None:
            function = lambda: self.parentApp.switchFormPrevious()

        self.add(EmptyLine)
        self.add(EmptyLine)
        self.add(Button, name=name, function=function)

    def addHeadline(self, name):
        self.add(EmptyLine)
        self.add(HeadLine, value=name)
        self.add(EmptyLine)

    def addField(self, name, kind = EntryField, indent=1, **kwargs):
        default_indent = 2

        if indent > 0:
            kwargs.update({'relx': default_indent + (indent * 5)})

        return self.add(kind, name=name, **kwargs)

    def create(self):
        self.addReturnButton()

class App(npyscreen.NPSAppManaged):
    def __init__(self):
        super(App, self).__init__()
        self.log = log_function(self)

    def onCleanExit(self):
        self.log('exiting')
        close_log()

    def print_log(self):
        print_log()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8