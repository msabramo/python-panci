import unittest

from panci.ciconfig import TravisPythonEnv, ToxPythonEnv, convert_env_list


class ToxPythonEnvTests(unittest.TestCase):

    def test_py24(self):
        env = ToxPythonEnv('py24')
        self.assertEqual(env.executable, 'python2.4')
        self.assertEqual(env.name, 'py24')

    def test_py25(self):
        env = ToxPythonEnv('py25')
        self.assertEqual(env.executable, 'python2.5')
        self.assertEqual(env.name, 'py25')

    def test_py26(self):
        env = ToxPythonEnv('py26')
        self.assertEqual(env.executable, 'python2.6')
        self.assertEqual(env.name, 'py26')

    def test_py27(self):
        env = ToxPythonEnv('py27')
        self.assertEqual(env.executable, 'python2.7')
        self.assertEqual(env.name, 'py27')

    def test_py30(self):
        env = ToxPythonEnv('py30')
        self.assertEqual(env.executable, 'python3.0')
        self.assertEqual(env.name, 'py30')

    def test_py31(self):
        env = ToxPythonEnv('py31')
        self.assertEqual(env.executable, 'python3.1')
        self.assertEqual(env.name, 'py31')

    def test_py32(self):
        env = ToxPythonEnv('py32')
        self.assertEqual(env.executable, 'python3.2')
        self.assertEqual(env.name, 'py32')

    def test_pypy(self):
        env = ToxPythonEnv('pypy')
        self.assertEqual(env.executable, 'pypy')
        self.assertEqual(env.name, 'pypy')

    def test_jython(self):
        env = ToxPythonEnv('jython')
        self.assertEqual(env.executable, 'jython')
        self.assertEqual(env.name, 'jython')


class TravisPythonEnvTests(unittest.TestCase):

    def test_py25(self):
        env = TravisPythonEnv('2.5')
        self.assertEqual(env.executable, 'python2.5')
        self.assertEqual(env.name, '2.5')

    def test_py26(self):
        env = TravisPythonEnv('2.6')
        self.assertEqual(env.executable, 'python2.6')
        self.assertEqual(env.name, '2.6')

    def test_py27(self):
        env = TravisPythonEnv('2.7')
        self.assertEqual(env.executable, 'python2.7')
        self.assertEqual(env.name, '2.7')

    def test_py32(self):
        env = TravisPythonEnv('3.2')
        self.assertEqual(env.executable, 'python3.2')
        self.assertEqual(env.name, '3.2')

    def test_pypy(self):
        env = TravisPythonEnv('pypy')
        self.assertEqual(env.executable, 'pypy')
        self.assertEqual(env.name, 'pypy')


class ToxToTravisPythonEnvTests(unittest.TestCase):

    def test_py25(self):
        env = TravisPythonEnv(ToxPythonEnv('py25').executable)
        self.assertEqual(env.executable, 'python2.5')
        self.assertEqual(env.name, '2.5')

    def test_py26(self):
        env = TravisPythonEnv(ToxPythonEnv('py26').executable)
        self.assertEqual(env.executable, 'python2.6')
        self.assertEqual(env.name, '2.6')

    def test_py27(self):
        env = TravisPythonEnv(ToxPythonEnv('py27').executable)
        self.assertEqual(env.executable, 'python2.7')
        self.assertEqual(env.name, '2.7')

    def test_py32(self):
        env = TravisPythonEnv(ToxPythonEnv('py32').executable)
        self.assertEqual(env.executable, 'python3.2')
        self.assertEqual(env.name, '3.2')

    def test_pypy(self):
        env = TravisPythonEnv(ToxPythonEnv('pypy').executable)
        self.assertEqual(env.executable, 'pypy')
        self.assertEqual(env.name, 'pypy')

    def test_tox_to_travis_list_1(self):
        tox_env_list = ['py24', 'py25', 'py26', 'py27', 'py30', 'py31', 'py32', 'pypy', 'jython']
        expected_travis_env_list = ['2.5', '2.6', '2.7', '3.2', 'pypy']
        travis_env_list = convert_env_list(ToxPythonEnv, TravisPythonEnv, tox_env_list)
        self.assertEqual(travis_env_list, expected_travis_env_list)

    def test_tox_to_travis_list_2(self):
        tox_env_list = ['py26', 'py27', 'py32', 'pypy', 'jython']
        expected_travis_env_list = ['2.6', '2.7', '3.2', 'pypy']
        travis_env_list = convert_env_list(ToxPythonEnv, TravisPythonEnv, tox_env_list)
        self.assertEqual(travis_env_list, expected_travis_env_list)

    def test_tox_to_travis_list_3(self):
        tox_env_list = ['py24', 'pypy', 'jython']
        expected_travis_env_list = ['pypy']
        travis_env_list = convert_env_list(ToxPythonEnv, TravisPythonEnv, tox_env_list)
        self.assertEqual(travis_env_list, expected_travis_env_list)

    def test_tox_to_travis_list_4(self):
        tox_env_list = ['py24', 'jython', 'abc']
        expected_travis_env_list = []
        travis_env_list = convert_env_list(ToxPythonEnv, TravisPythonEnv, tox_env_list)
        self.assertEqual(travis_env_list, expected_travis_env_list)

    def test_tox_to_travis_list_5(self):
        tox_env_list = ['']
        expected_travis_env_list = []
        travis_env_list = convert_env_list(ToxPythonEnv, TravisPythonEnv, tox_env_list)
        self.assertEqual(travis_env_list, expected_travis_env_list)

    def test_travis_to_tox_list_1(self):
        travis_env_list = ['2.5', '2.6', '2.7', '3.2', 'pypy']
        expected_tox_env_list = ['py25', 'py26', 'py27', 'py32', 'pypy']
        tox_env_list = convert_env_list(TravisPythonEnv, ToxPythonEnv, travis_env_list)
        self.assertEqual(tox_env_list, expected_tox_env_list)

    def test_travis_to_tox_list_2(self):
        travis_env_list = ['2.5', '2.6', '2.7', '3.2', '3.3', 'pypy']
        expected_tox_env_list = ['py25', 'py26', 'py27', 'py32', 'py33', 'pypy']
        tox_env_list = convert_env_list(TravisPythonEnv, ToxPythonEnv, travis_env_list)
        self.assertEqual(tox_env_list, expected_tox_env_list)

    def test_travis_to_tox_list_3(self):
        travis_env_list = []
        expected_tox_env_list = []
        tox_env_list = convert_env_list(TravisPythonEnv, ToxPythonEnv, travis_env_list)
        self.assertEqual(tox_env_list, expected_tox_env_list)


class TravisToToxPythonEnvTests(unittest.TestCase):

    def test_py25(self):
        env = ToxPythonEnv(TravisPythonEnv('2.5').executable)
        self.assertEqual(env.executable, 'python2.5')
        self.assertEqual(env.name, 'py25')

    def test_py26(self):
        env = ToxPythonEnv(TravisPythonEnv('2.6').executable)
        self.assertEqual(env.executable, 'python2.6')
        self.assertEqual(env.name, 'py26')

    def test_py27(self):
        env = ToxPythonEnv(TravisPythonEnv('2.7').executable)
        self.assertEqual(env.executable, 'python2.7')
        self.assertEqual(env.name, 'py27')

    def test_py32(self):
        env = ToxPythonEnv(TravisPythonEnv('3.2').executable)
        self.assertEqual(env.executable, 'python3.2')
        self.assertEqual(env.name, 'py32')

    def test_pypy(self):
        env = ToxPythonEnv(TravisPythonEnv('pypy').executable)
        self.assertEqual(env.executable, 'pypy')
        self.assertEqual(env.name, 'pypy')

