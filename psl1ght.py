#!/usr/bin/env python

def update(cd, run):
    cd('PSL1GHT')
    run(['git pull -u'])
    cd('..')

def download(cd, run):
    run(['git', 'clone', 'https://github.com/HACKERCHANNEL/PSL1GHT.git'])

def build(cd, run):
    cd('PSL1GHT')
    run(['make'])
    run(['make install'])
    cd('..')
