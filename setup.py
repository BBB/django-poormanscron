#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-poormanscron',
    version='0.1.3',
    author=u'Bruno Renié & Ollie Relph',
    author_email='aidas.bendoraitis@gmail.com & ollie@relph.me',
    packages=find_packages(),
    url='https://github.com/BBB/django-poormanscron/tree/master/',
    license='BSD',
    description='Poor Man\'s Cron is Django app which makes use of spambots, search engine indexing robots and alike to run scheduled tasks in approximately regular intervals.',
    # long_description=open('README.md').read(),
    zip_safe=False,
)