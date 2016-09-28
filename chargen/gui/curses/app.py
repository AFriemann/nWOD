# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import npyscreen

from chargen.gui.logger import Logger

class App(npyscreen.NPSAppManaged):
    def onCleanExit(self):
        with Logger(self) as log:
            log('exiting')
        Logger.close_log()

    def print_log(self):
        Logger.print_log()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
