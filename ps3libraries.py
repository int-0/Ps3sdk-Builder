#!/usr/bin/env python

def update(cd, run):
    cd('ps3libraries')
    run(['git pull -u'])
    cd('..')

def download(cd, run):
    run(['git', 'clone', 'https://github.com/ooPo/ps3libraries.git'])

def build(cd, run):
    cd('ps3libraries')
    run(['./libraries.sh'])
    cd('..')
