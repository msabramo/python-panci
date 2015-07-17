import six
import unittest

from panci.travis2tox import travis2tox


class TravisToToxCommandsTests(unittest.TestCase):

    def test_before_install(self):
        travis = '''
language: python
python:
  - 2.7
before_install:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])

    def test_install(self):
        travis = '''
language: python
python:
  - 2.7
install:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])

    def test_after_install(self):
        travis = '''
language: python
python:
  - 2.7
after_install:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])

    def test_before_script(self):
        travis = '''
language: python
python:
  - 2.7
before_script:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])

    def test_script(self):
        travis = '''
language: python
python:
  - 2.7
script:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])

    def test_after_script(self):
        travis = '''
language: python
python:
  - 2.7
script:
  - echo 1
  - echo 2
        '''

        tox_config = travis2tox(six.StringIO(travis))
        self.assertEqual(tox_config.commands, ['echo 1', 'echo 2'])
