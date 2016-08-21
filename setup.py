#!/usr/bin/env python

from setuptools import setup

setup(
    name='flask_ext_migrate',
    version='0.1.0',
    url='https://github.com/pallets/flask-ext-migrate',
    license='BSD',
    author='Keyan Pishdadian',
    author_email='kpishdadian@gmail.com',
    description='A sourcecode manipulation tool for converting imports.',
    long_description='This tool allows for rapid migration of extension '
                     'imports away from the deprecated `.ext` format.',
    install_requires=['RedBaron', 'click'],
    tests_require=['nose'],
    packages=['flask_ext_migrate'],
    entry_points={
        'console_scripts': [
            'flask_ext_migrate = flask_ext_migrate.startup:startup']
    }
)
