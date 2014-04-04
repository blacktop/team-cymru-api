try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

setup(
    name='cymru-api',
    test_suite="tests",
    version='1',
    packages=['team_cymru', 'team_cymru.test'],
    url='https://github.com/blacktop/cymru-api',
    license='GPLv3',
    author='blacktop',
    author_email='',
    description='Team Cymru - Malware Hash Registry API',
    install_requires=[
        "requests >= 2.2.1",
    ],
)
