#!/usr/bin/env python

import os
import os.path
import subprocess

# Directory related tools
def dir_default():
    return '/usr/local/ps3dev2'

def dir_exists(directory):
    return os.path.isdir(directory)

def dir_toplevel(directory):
    return os.path.basename(directory)

def dir_base(directory):
    return os.path.dirname(directory)

def dir_current():
    return os.getcwd()

def dir_create(directory):
    os.makedirs(directory, 0775)

def dir_change(directory):
    os.chdir(directory)

def file_exists(filename):
    return os.path.isfile(filename)

def at_home(path):
    return os.path.join(os.path.expanduser('~'), path)

def modify_bashrc(directory):
    fd = open(at_home('.bashrc'), 'a')
    fd.write('# Added by Ps3Builder\n')
    fd.write('export PS3DEV=' + directory + '\n')
    fd.write('export PSL1GHT=' + os.path.join(directory, 'psl1ght') + '\n')
    fd.write('export PATH=$PATH:$PS3DEV/bin\n')
    fd.write('export PATH=$PATH:$PS3DEV/ppu/bin\n')
    fd.write('export PATH=$PATH:$PS3DEV/spu/bin\n')
    fd.write('# End modifications by Ps3Builder\n')
    fd.close()

def set_environment(directory):
    os.environ['PS3DEV'] = directory
    os.environ['PSL1GHT'] = os.path.join(directory, 'psl1ght')
    os.environ['PATH'] = os.environ['PATH'] + ':' + os.path.join(directory,
                                                                 'bin')
    os.environ['PATH'] = os.environ['PATH'] + ':' + os.path.join(directory,
                                                                 'ppu/bin')
    os.environ['PATH'] = os.environ['PATH'] + ':' + os.path.join(directory,
                                                                 'spu/bin')

def run(command):
    pid = subprocess.Popen(command)
    pid.wait()

def run_nowait(command):
    run(command)
