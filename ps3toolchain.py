#!/usr/bin/env python

def update(cd, run):
    cd('ps3toolchain')
    run(['git pull -u'])
    cd('..')

def download(cd, run):
    run(['git', 'clone', 'https://github.com/ooPo/ps3toolchain.git'])

def build(cd, run):
    cd('ps3toolchain')
    run(['./toolchain.sh'])
    cd('..')

