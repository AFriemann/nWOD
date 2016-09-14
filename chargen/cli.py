# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import click

from . import __version__

from .model.character import Character, VIRTUES, VICES

def split_focus_string(string):
    return string.split('/')

@click.command()
@click.option('--name', prompt=True)
@click.option('--age', type=int, prompt=True)
@click.option('--virtue', type=click.Choice(VIRTUES), prompt=True)
@click.option('--vice', type=click.Choice(VICES), prompt=True)
@click.option('--attribute-focus', type=split_focus_string, prompt=True, help='Mental/Physical/Social')
def main(name, age, virtue, vice, attribute_focus):
    char = Character(
        Name = name,
        Age  = age,
        Virtue = virtue,
        Vice   = vice,
    )

    print(dict(char))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
