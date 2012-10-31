#!/usr/bin/env python

"""
Program for converting between different CI config files, like `.travis.yml`
and `tox.ini`.

"""

import argparse

from panci.travis2tox import travis2tox
from panci.tox2travis import tox2travis


def main():
    """The ``main`` for the ``panci`` program."""

    parser = argparse.ArgumentParser(
        description='Convert a .travis.yml file to a tox.ini file or vice-versa.')
    parser.add_argument(
        '-t', '-w', '--to', '--write',
        metavar='FORMAT',
        help='output format')
    parser.add_argument(
        'input_file',
        help='path to a .travis.yml or tox.ini file')
    args = parser.parse_args()

    if args.to == 'tox' or args.input_file.endswith('.yml'):
        tox_config = travis2tox(args.input_file)
        print(tox_config.getvalue())
    elif args.to == 'travis' or args.input_file.endswith('.ini'):
        travis_config = tox2travis(args.input_file)
        print(travis_config)


if __name__ == '__main__':
    main()
