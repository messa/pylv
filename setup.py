#!/usr/bin/env python

from setuptools import setup

setup(
    name='pylv',
    version='0.0.1',
    description='Helper that locates virtualenv',
    url='https://github.com/messa/pylv',
    author='Petr Messner',
    author_email='petr.messner@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    py_modules=['pylv'],
    entry_points={
        'console_scripts': [
            'pylv=pylv:main',
            'py2lv=pylv:main',
            'py3lv=pylv:main',
        ],
    })
