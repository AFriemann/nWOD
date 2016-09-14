#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

# import logging
# logging.basicConfig(level=logging.DEBUG)

from . import gui

if __name__ == '__main__':
    try:
        exit(gui.main())
    except KeyboardInterrupt:
        exit(137)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
