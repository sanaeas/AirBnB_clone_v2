#!/usr/bin/python3
"""Fabric script to generate a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the web_static folder"""
    if not os.path.exists("versions"):
        os.mkdir("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = "versions/web_static_{}.tgz".format(timestamp)

    file = local("tar -cvzf {} web_static".format(archive_filename))
    if file is not None:
        return archive_filename
    else:
        return None
