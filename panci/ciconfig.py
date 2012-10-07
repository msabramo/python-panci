import re


def convert_env_list(src_env_class, dst_env_class, src_env_names):
    def get_dst_env(src_env_name):
        return dst_env_class(src_env_class(src_env_name).executable)

    dst_envs = map(get_dst_env, src_env_names)

    return [dst_env.name for dst_env in dst_envs if dst_env.name]


class AbstractPythonEnv(object):
    """Abstraction of list of Pythons to run against -- e.g.:
       - Travis: 2.5, 2.6, 2.7, 3.2, pypy
       - Tox: py25, py26, py27, py32, pypy, jython

    """

    executable = ''

    def __init__(self, s):
        pass

    @property
    def name(self):
        pass


class TravisPythonEnv(AbstractPythonEnv):

    regex = '(?P<major_version>\d)\.(?P<minor_version>\d)'

    def __init__(self, s):
        match = re.match(self.regex, s)

        if match:
            group_dict = match.groupdict()
            major_version = int(group_dict['major_version'])
            minor_version = int(group_dict['minor_version'])
            self.executable = 'python%d.%d' % (major_version, minor_version)
        else:
            self.executable = s

    @property
    def name(self):
        if self.executable in ('python2.5', 'python2.6', 'python2.7', 'python3.2', 'pypy'):
            return self.executable.replace('python', '')


class ToxPythonEnv(AbstractPythonEnv):

    regex = 'py(?P<major_version>\d)(?P<minor_version>\d)'

    def __init__(self, s):
        match = re.match(self.regex, s)

        if match:
            group_dict = match.groupdict()
            self.major_version = int(group_dict['major_version'])
            self.minor_version = int(group_dict['minor_version'])
            self.executable = 'python%d.%d' % (self.major_version, self.minor_version)
        else:
            self.executable = s

    @property
    def name(self):
        if self.executable in ('pypy', 'jython'):
            return self.executable
        else:
            regex = 'python(?P<major_version>\d)\.(?P<minor_version>\d)'
            match = re.match(regex, self.executable)

            if match:
                group_dict = match.groupdict()
                major_version = int(group_dict['major_version'])
                minor_version = int(group_dict['minor_version'])

            return 'py%d%d' % (major_version, minor_version)


class EnvList(object):
    """Abstraction of list of Pythons to run against -- e.g.:
       - Travis: 2.5, 2.6, 2.7, 3.2, pypy
       - Tox: py25, py26, py27, py32, pypy, jython

    """
    pass


class CIConfig(object):

    @classmethod
    def from_file(cls, f):
        pass

    def get_envlist(self):
        """Return an ``Envlist``?"""
        pass

    def get_commands(self):
        pass


class TravisCIConfig(CIConfig):
    pass

class ToxCIConfig(CIConfig):
    pass
