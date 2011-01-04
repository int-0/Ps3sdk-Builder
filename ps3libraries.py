#!/usr/bin/env python

def update(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('ps3libraries')
    run(['git pull -u'])
    cd('..')

def download(os_helper):
    run = os_helper.run
    run(['git', 'clone', 'https://github.com/ooPo/ps3libraries.git'])

def build(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('ps3libraries')
    run(['./libraries.sh'])
    cd('..')
