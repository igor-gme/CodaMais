#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session='hack')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='CodaMais',
      version='1.0',
      description='CodaMais is a web platform whose purpose is to teach calculation logic to use a C language.',
      author='Igor Gabriel',
      install_requires=reqs,
      license='GNU GENERAL PUBLIC LICENSE Version 3 ',
      platforms='Web',
      author_email='igorgabriel515@gmail.com',
      url='gcs-codamais-igor.herokuapp.com',
      packages=find_packages(),
      )
