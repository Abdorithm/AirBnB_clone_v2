#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import time
import os


env.hosts = ['35.175.104.84', '100.26.151.210']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p versions")
    archive_path = 'versions/web_static_{}.tgz'.format(
        time.strftime('%Y%m%d%H%M%S'))
    results = local('tar -cvzf {} web_static'.format(archive_path))
    if results.successed:
        return archive_path
    return None


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_file = archive_path[9:]
    release_version = '/data/web_static/releases/{}'.format(archive_file[:-4])
    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(release_version))
    run('tar -xzf /tmp/{} -C {}'.format(archive_file, release_version))
    run('rm /tmp/{}'.format(archive_file))
    run('sudo mv {}/web_static/* {}'.format(release_version, release_version))
    run('sudo rm -rf /data/web_static/releases/web_static')
    run('sudo rm -rf /data/web_static/current')
    run('sudo ln -s {} /data/web_static/current'.format(release_version))

    print('New version deployed!')
    return True


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
