#!/usr/bin/python3
"""Fabric script to deploy an archive to web servers"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.25.136.168', '100.26.9.198']


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(
                           archive_filename.split('.')[0])
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))

        run('rm /tmp/{}'.format(archive_filename))

        run('mv {}/web_static/* {}'.format(archive_folder, archive_folder))

        run('rm -rf {}/web_static'.format(archive_folder))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(archive_folder))

        return True
    except Exception:
        return False
