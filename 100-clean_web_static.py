#!/usr/bin/python3
""" Defines do_clean function """
from fabric.api import *

env.hosts = ['35.175.104.84', '100.26.151.210']
env.user = 'ubuntu'


def do_clean(number=0):
    """ deletes out-of-date archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
