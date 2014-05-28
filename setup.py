#!/usr/bin/env python
import os
import sys

import team_cymru_api

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('doc/README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(name='team-cymru-api'
        ,version=team_cymru_api.__version__
        ,description='Team Cymru - Malware Hash Registry API'
        ,long_description=readme + '\n\n' + history
        ,url='https://github.com/blacktop/team-cymru-api'
        ,author='blacktop'
        ,author_email='dev@blacktop.io'
        ,license=team_cymru_api.__license__
        ,test_suite="tests"
        ,packages=['team_cymru_api']
        ,package_dir={'team_cymru_api': 'team_cymru_api'})
