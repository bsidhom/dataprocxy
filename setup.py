# Copyright (c) 2015 Spotify AB
from setuptools import setup

setup(name='dataprocxy',
      version='0.1',
      description='using a dataproc job or cluster id and a project, open a browser to important URLs using an ssh SOCKS proxy',
      url='https://github.com/spotify/dataprocxy',
      author='Johannes Russek',
      author_email='jrussek@spotify.com',
      license='Apache 2.0',
      packages=['dataprocxy'],
      install_requires=['google-api-python-client'],
      scripts=['bin/dataprocxy'],
      zip_safe=False)
