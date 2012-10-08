panci
==========

.. image:: https://secure.travis-ci.org/msabramo/python-panci.png
   :target: http://travis-ci.org/msabramo/python-panci

For a Python project, take a ``.travis.yml`` file (`Travis CI`_) and output a
``tox.ini`` file (`Tox`_). Or vice-versa.

Example
-------

Travis to Tox
~~~~~~~~~~~~~

Let's say that we have the following ``.travis.yml``::

    language: python

    python:
      - 2.6
      - 2.7
      - 3.2
      - pypy

    script: python setup.py test

If we run::

    panci --to=tox .travis.yml

Then we get::

    # Tox (http://tox.testrun.org/) is a tool for running tests
    # in multiple virtualenvs. This configuration file will run the
    # test suite on all supported python versions. To use it, "pip install tox"
    # and then run "tox" from this directory.

    [tox]
    envlist = py26, py27, py32, pypy

    [testenv]
    commands = python setup.py test

Tox to Travis
~~~~~~~~~~~~~

Let's say that we have the following ``tox.ini``::

	# Tox (http://tox.testrun.org/) is a tool for running tests
	# in multiple virtualenvs. This configuration file will run the
	# test suite on all supported python versions. To use it, "pip install tox"
	# and then run "tox" from this directory.

	[tox]
	envlist = py25, py26, py27, py32, py33, pypy, jython

	[testenv]
	commands = {envpython} setup.py test

If we run::

	panci --to=travis tox.ini
	
Then we get::

	language: python
	python:
	- '2.5'
	- '2.6'
	- '2.7'
	- '3.2'
	- '3.3'
	- pypy
	script: '{envpython} setup.py test'

For questions, comments, and suggestions, please use `GitHub Issues`_.

.. _Travis CI: http://travis-ci.org/
.. _Tox: http://tox.testrun.org/
.. _GitHub Issues: https://github.com/msabramo/python-panci/issues
