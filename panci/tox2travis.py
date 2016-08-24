"""Utilities for converting from Travis CI configs to Tox configs."""

import textwrap

from .toxconfig import ToxConfig


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
          - travis_retry pip install tox
        script:
          - travis_retry tox
        """.format(env_list=env_list)).strip()
