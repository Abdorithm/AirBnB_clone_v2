#!/usr/bin/python3
""" Defines do_clean function """
from fabric.api import *

env.hosts = ['52.204.168.90', '100.26.50.2']
env.user = 'ubuntu'


def do_clean(number=0):
    """ deletes out-of-date archives """
    number = int(number)
    path = '/data/web_static/releases'

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
