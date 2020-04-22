#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the
    contents of the web_static folder of
    your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    Archive:
    web_static_<year><month><day><hour><minute><second>.tgz
    Return:
    Return the path if the archive has been correctly generated
    otherwise, return None
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path_name = "versions/web_static_{}.tgz".format(time)
    tar_status = local("tar -cvzf {} web_static".format(path_name))
    return path_name if tar_status.succeeded else None


if __name__ == '__main__':
    do_pack()
