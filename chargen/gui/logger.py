# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

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
        logfd.flush()

    @staticmethod
    def close_log():
        logfd.flush()
        logfd.close()

    @staticmethod
    def print_log():
        with open(LOGFILE, 'rb') as stream:
            content = stream.read().decode()
        print(content)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
