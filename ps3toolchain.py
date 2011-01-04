#!/usr/bin/env python

def update(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('ps3toolchain')
    run(['git pull -u'])
    cd('..')

def download(os_helper):
    run = os_helper.run
    run(['git', 'clone', 'https://github.com/ooPo/ps3toolchain.git'])

def build(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('ps3toolchain')
    run(['./toolchain.sh'])
    cd('..')

