#!/usr/bin/python3
"""
Fabric script to automate cleaning of outdated archives
"""
from fabric.api import local, env, run, lcd
import os

env.hosts = ['100.25.136.168', '100.26.9.198']


def do_clean(number=0):
    """
    Delete outdated archives and keeps the specified number
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    with lcd("versions"):
        archives = sorted(os.listdir("."))
        archives_to_delete = archives[:-number]
        [local("rm -f {}".format(archive)) for archive in archives_to_delete]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr | grep 'web_static_'").split()
        archives_to_delete = archives[:-number]
        [run("rm -rf {}".format(archive)) for archive in archives_to_delete]
