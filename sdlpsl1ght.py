#!/usr/bin/env python

def update(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('SDL_PSL1GHT')
    run(['git pull -u'])
    cd('..')

def download(os_helper):
    run = os_helper.run
    run(['git', 'clone', 'https://github.com/cebash/SDL_PSL1GHT.git'])

def build(os_helper):
    cd = os_helper.dirs.change
    run = os_helper.run
    cd('SDL_PSL1GHT')
    run(['./script.sh'])
    run(['make'])
    run(['make install'])
    cd('..')
