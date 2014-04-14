#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Josh Maine'
__version__ = '1'
__license__ = 'GPLv3'

from unittest import TestCase
from team_cymru.team_cymru_api import TeamCymruApi


class InitTests(TestCase):
    def test_hash_found(self):
        myteam = TeamCymruApi()

        try:
            print myteam.get_cymru('039ea049f6d0f36f55ec064b3b371c46')
        except Exception as e:
            self.fail(e)

    def test_hash_not_found(self):
        myteam = TeamCymruApi()

        try:
            print myteam.get_cymru('5e28284f9b5f9097640d58a73d38ad4c')
        except Exception as e:
            self.fail(e)

    def test_hash_bad_input(self):
        myteam = TeamCymruApi()

        try:
            print myteam.get_cymru(False)
        except Exception as e:
            self.fail(e)