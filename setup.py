#!/usr/bin/env python
from setuptools import setup, find_packages

setup(version='0.1',
        name='md_jinja2',
        description='Markdown Extension for Jinja2',
        packages=find_packages(),
        install_requires=[
            'jinja2',
            'markdown'
        ],
        )
