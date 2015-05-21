#!/usr/bin/env python

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

    path = ''
    for i in range(os.getcwd().count(sep)):
        for vn in venv_names:
            exec_path = path + vn + '/bin/' + exec_name
            if isfile(exec_path):
                # found it!
                exec_args = [exec_path] + sys.argv[1:]
                os.execv(exec_path, exec_args)
        path += '..' + sep
    sys.exit('%s: failed to locate Python virtual env (venv_names: %r, exec_name: %r)' % (
        our_name, venv_names, exec_name))


if __name__ == '__main__':
    main()
