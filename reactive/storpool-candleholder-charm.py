"""
A Juju charm that does nothing.
"""

from __future__ import print_function

from charms import reactive

from charmhelpers.core import hookenv


@reactive.hook('install')
def first_install():
    """
    Just say "hi".
    """
    hookenv.log('Hello, cruel world!', hookenv.INFO)
    hookenv.status_set('maintenance', 'setting up')


@reactive.hook('start')
def start():
    """
    Well... yeah.
    """
    hookenv.log('I am still here!', hookenv.INFO)
    hookenv.status_set('active', 'bring on the subordinate charms!')
