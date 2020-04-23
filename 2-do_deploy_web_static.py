#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""


from fabric.api import local, run, env, put
from datetime import datetime
import logging

logger = logging.getLogger('ftpuploader')
env.hosts = ['34.73.17.45 ']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


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


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    Return:
        False if the file at the path archive_path doesnt exist
    """

    file_name = archive_path.split('/')[1]
    file_noext = file_name.split('.')[0]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(file_noext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(file_name, file_noext))
        run('rm /tmp/{}'.format(file_name))
        run('mv -f /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(file_noext, file_noext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_noext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} \
        /data/web_static/current'.format(file_noext))
        print('New version deployed!')
        return True

    except Exception as e:
        # Checks for errors
        logger.error(str(e))
        print('New version has not been deployed...')
        return False


if __name__ == '__main__':
    do_deploy()