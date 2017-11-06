#!/usr/bin/python3

"""
A set of unit tests for the storpool-candleholder charm that
does nothing yet allows other charms to attach to it.
"""

import os
import sys
import testtools

import mock


lib_path = os.path.realpath('.')
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)


from reactive import storpool_candleholder_charm as testee


class TestCandleHolder(testtools.TestCase):
    @mock.patch('charmhelpers.core.hookenv.status_set')
    @mock.patch('charmhelpers.core.hookenv.log')
    def test_candleholder(self, h_log, h_status_set):
        """
        Test the two routines in the candleholder charm.
        """

        testee.first_install()
        self.assertEquals(h_log.call_count, 1)
        self.assertEquals(h_status_set.call_count, 1)

        testee.start()
        self.assertEquals(h_log.call_count, 2)
        self.assertEquals(h_status_set.call_count, 2)
