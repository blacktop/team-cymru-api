try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

setup(
    name='team-cymru-api',
    test_suite="tests",
    version='1.0.1',
    packages=['team_cymru', 'team_cymru.test'],
    url='https://github.com/blacktop/team-cymru-api',
    license='GPLv3',
    author='blacktop',
    author_email='dev@blacktop.io',
    description='Team Cymru - Malware Hash Registry API',
)
