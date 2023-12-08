#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import os


env.hosts = ['54.197.43.224', '52.201.178.140']


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    archive_file = archive_path[9:]
    release_version = '/data/web_static/releases/{}/'.format(archive_file[:-4])
    put('archive_path', 'tmp/{}'.format(archive_file))
    run('mkdir -p {}'.format(release_version))
    run('tar -xzf /tmp/{} -C {}'.format(archive_file, release_version))
    run('rm /tmp/{}'.format(archive_file))
    run('mv {}/web_static/* {}'.format(release_version, release_version))
    run('rm -rf /data/web_static/releases/web_static')
    run('ln -sf {} /data/web_static/current'.format(release_version))

    print('New version deployed!')
    return True
