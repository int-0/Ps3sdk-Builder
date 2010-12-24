#!/usr/bin/env python

def update(cd, run):
    cd('SDL_PSL1GHT')
    run(['git pull -u'])
    cd('..')

def download(cd, run):
    run(['git', 'clone', 'https://github.com/cebash/SDL_PSL1GHT.git'])

def build(cd, run):
    cd('SDL_PSL1GHT')
    run(['./script.sh'])
    run(['make'])
    run(['make install'])
    cd('..')
