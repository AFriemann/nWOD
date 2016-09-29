# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import logging, ruamel.yaml as pyaml

from chargen.gui.app import CharacterGenerator

def run(default_dir = None):
    logger = logging.getLogger(__name__)

    chargen = CharacterGenerator(default_dir)
    chargen.run()

    chargen.print_log()

    try:
        print(pyaml.safe_dump(dict(chargen), default_flow_style=False))
    except Exception as e:
        logger.exception(e)
        print('Created character invalid')
        return 1

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
