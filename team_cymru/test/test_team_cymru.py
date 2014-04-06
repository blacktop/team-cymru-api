#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh Maine'

from team_cymru.team_cymru_api import TeamCymruApi

myteam = TeamCymruApi()
print myteam.get_cymru('039ea049f6d0f36f55ec064b3b371c46')
print myteam.get_cymru('5e28284f9b5f9097640d58a73d38ad4c')
print