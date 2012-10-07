panci
==========

.. image:: https://secure.travis-ci.org/msabramo/python-panci.png
   :target: http://travis-ci.org/msabramo/python-panci

For a Python project, take a ``.travis.yml`` file (`Travis CI`_) and output a
``tox.ini`` file (`Tox`_).

Example
-------

::

    $ cat .travis.yml
    language: python

    python:
      - 2.6
      - 2.7
      - 3.2
      - pypy

    script: python setup.py test

    $ panci -t tox .travis.yml
    # Tox (http://tox.testrun.org/) is a tool for running tests
    # in multiple virtualenvs. This configuration file will run the
    # test suite on all supported python versions. To use it, "pip install tox"
    # and then run "tox" from this directory.

    [tox]
    envlist = py26, py27, py32, pypy

    [testenv]
    commands = python setup.py test

.. _Travis CI: http://travis-ci.org/
.. _Tox: http://tox.testrun.org/
