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
    if int(number) < 1:
        number = 1
    number = int(number) + 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number))
