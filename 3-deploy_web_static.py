#!/usr/bin/python3
"""
Fabric script to automate deployment of web_static content
"""
from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ['100.25.136.168', '100.26.9.198']


def do_pack():
    """
    Compresses web_static folder and stores it in versions/
    """
    try:
        local('mkdir -p versions')
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(timestamp)
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploys the web_static content to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        no_extension = filename.split('.')[0]
        remote_path = '/data/web_static/releases/{}/'.format(no_extension)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(remote_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, remote_path))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(remote_path, remote_path))
        run('rm -rf {}web_static'.format(remote_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))
        return True
    except Exception:
        return False


def deploy():
    """
    Calls do_pack() and do_deploy() to deploy the web_static content
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
