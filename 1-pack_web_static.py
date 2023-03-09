#!/usr/bin/python3
"""fabric script that generates a .tgz"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """returns the archive path"""
    try:
        date_format = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(date_format)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None
