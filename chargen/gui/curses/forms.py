# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import npyscreen

from chargen.gui.curses.logger import Logger

from chargen.gui.curses.elements import *

class Form(npyscreen.FormBaseNewWithMenus):
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

    def addButton(self, name, function):
        self.add(Button, name=name, function=function)

    def addHeadline(self, name):
        self.add(HeadLine, value=name)
        self.add(EmptyLine)

    def addLink(self, name, target, indent=0, **kwargs):
        if indent > 0:
            kwargs.update({'relx': self.default_indent + (indent * self.indent_step)})

        return self.add(Link, name=name, target=target, **kwargs)

    def addEmptyLine(self):
        self.add(EmptyLine)

    def addField(self, name, kind = EntryField, indent=0, **kwargs):
        if indent > 0:
            kwargs.update({'relx': self.default_indent + (indent * self.indent_step)})

        return self.add(kind, name=name, **kwargs)

    def addFieldGroup(self, name, **kwargs):
        self.addHeadline(name)

        group = { k: self.addField(**v) for k,v in kwargs.items() }
        self.__setattr__('group_%s' % name.lower(), group)

        return group

    def create(self):
        self.addReturnButton()

    def get_group(self, name):
        return vars(self)['group_%s' % name]

    def get_field(self, name):
        return vars(self)['field_%s' % name]

    def get_fields(self):
        return [ (k.replace('field_', ''), v) for k,v in vars(self).items() if k.startswith('field_') ]

    def get_field_groups(self):
        return [ (k.replace('group_', ''), v) for k,v in vars(self).items() if k.startswith('group_') ]

    def get_items(self):
        items = {}

        for field,proxy in self.get_fields():
            items[field] = proxy.get_value()

        for group,fields in self.get_field_groups():
            items[group] = { name: proxy.get_value() for name,proxy in fields.items() }

        return items

    def set_fields(self, **kwargs):
        for name, proxy in self.get_fields():
            if name in kwargs:
                proxy.set_value(kwargs.get(name))

    def set_field_groups(self, **kwargs):
        for group, proxies in self.get_field_groups():
            if group in kwargs:
                values = kwargs.get(group)
                for field, proxy in proxies.items():
                    if field in values:
                        proxy.set_value(values.get(field))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
