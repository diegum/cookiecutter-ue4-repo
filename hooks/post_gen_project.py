#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess


def execute_shell_command(cmd):
    """Executes a shell command in a subprocess, waiting until it has completed.

    :param cmd: Command to execute.
    """

    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print out, error
    pipe.wait()


git_init = 'git init'
git_add = 'git add --all'
git_commit = 'git commit -am "%s"' % 'Initial commit.'

execute_shell_command(git_init)
execute_shell_command(git_add)
execute_shell_command(git_commit)
