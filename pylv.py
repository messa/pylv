#!/usr/bin/env python

'''
This script is intended to be used in shebang for running other scripts
- '#!/usr/bin/env pylv' instead of '#!/usr/bin/env python'.

Its effect is that the script will be run inside a virtual environment.
The virtual environment is searched from the current working directory up,
its name is expected to be 'venv'.
'''

import os
from os.path import basename, isfile, sep
import sys


venv_names = ['venv']


def main():
    exec_name = 'python'
    our_name = basename(sys.argv[0])
    if our_name.startswith('py3'):
        exec_name = 'python3'
    elif our_name.startswith('py2'):
        exec_name = 'python2'

    already_in_venv = bool(os.environ.get('VIRTUAL_ENV'))
    if already_in_venv:
        # we will not be looking for another virtual env;
        # just run the script
        exec_args = [exec_name] + sys.argv[1:]
        os.execvp(exec_name, exec_args)
        assert None, "os.exec doesn't return"

    path = ''
    for i in range(os.getcwd().count(sep)):
        for vn in venv_names:
            exec_path = path + vn + '/bin/' + exec_name
            if isfile(exec_path):
                # found it!
                exec_args = [exec_path] + sys.argv[1:]
                os.execv(exec_path, exec_args)
                assert None, "os.exec doesn't return"
        path += '..' + sep

    # nothing found
    sys.exit('%s: failed to locate Python virtual env (venv_names: %r, exec_name: %r)' % (
        our_name, venv_names, exec_name))


if __name__ == '__main__':
    main()
