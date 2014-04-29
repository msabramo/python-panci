"""Utilities for converting from Travis CI configs to Tox configs."""

import textwrap

from .travisconfig import TravisConfig
from .toxconfig import ToxConfig


def travis_env_to_tox_env(travis_env):
    """Converts a Travis-style environment (e.g.: "2.6") to a Tox-style
    environment (e.g.: "py26")."""

    travis_env = str(travis_env)

    if not travis_env.startswith('py') and travis_env[1] == '.':
        return 'py' + travis_env.replace('.', '')
    else:
        return travis_env


def tox_envlist_to_travis_envlist(tox_envlist):
    """Converts Tox-style environments (e.g.: "py26") to a Travis-style
    environments (e.g.: "2.6")."""

    travis_envlist = []

    for env in tox_envlist:
        if env.startswith('py'):
            if env == 'pypy':
                travis_envlist.append(env)
            else:
                travis_envlist.append(env[2] + '.' + env[3])

    return travis_envlist


def travis2tox(in_file):
    """Takes a path or file object for a ``.travis.yml`` file and returns a
    ``ToxConfig`` object."""

    config = TravisConfig(in_file)
    envlist = map(travis_env_to_tox_env, config.python)
    commands = config.get_all_commands()

    return ToxConfig(envlist, commands)


def tox2travis(in_file):
    config = ToxConfig.from_file(in_file)
    env_list = ('\n' + 10 * chr(32)).join([
        '- TOXENV={0}'.format(env) for env in config.envlist
    ])

    return textwrap.dedent("""
        language: python
        env:
          {env_list}
        install:
          - travis_retry pip install tox==1.6.1
        script:
          - travis_retry tox
        """.format(env_list=env_list)).strip()
