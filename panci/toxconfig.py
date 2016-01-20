"""Provides a ``ToxConfig`` class for operating on ``tox.ini`` files"""

import subprocess

try:
    # Python 2
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser

from string import Template


class ToxConfig(object):
    """Class for operating on ``tox.ini`` files"""

    @classmethod
    def from_file(cls, in_file):
        if not hasattr(in_file, 'read'):
            in_file = open(in_file, 'r')

        config_parser = ConfigParser()

        try:
            # Python 3
            config_parser.read_file(in_file)
        except AttributeError:
            # Python 2
            config_parser.readfp(in_file)

        return ToxConfig(
            envlist=cls._get_envlist_from_tox(in_file.name),
            commands=config_parser.get('testenv', 'commands')
        )

    @classmethod
    def _get_envlist_from_tox(cls, in_file):
        tox_l_output = subprocess.check_output(['tox', '-c', in_file, '-l'])
        return tox_l_output.splitlines()

    def __init__(self, envlist, commands):
        """Create an object from a list of environments and a list of
        commands."""

        self.envlist = envlist
        self.commands = commands

    def getvalue(self):
        """Return a string with the contents of a ``tox.ini`` file."""

        envlist = ', '.join(self.envlist)
        commands = self.get_commands()

        return Template("""
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
envlist = $envlist

[testenv]
commands = $commands
        """).substitute(
            envlist=envlist,
            commands=commands,
        ).lstrip()

    def get_commands(self):
        """Return a string with the content of the ``commands`` key for a
        ``tox.ini`` file."""

        commands = []

        if hasattr(self.commands, 'startswith'):
            commands.append(self.commands)
        elif hasattr(self.commands, '__getitem__'):
            commands.extend(self.commands)

        if len(commands) == 1:
            return commands[0]
        elif len(commands) > 1:
            return "\n    " + "\n    ".join(commands)
