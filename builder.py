#!/usr/bin/env python
#

import os
import sys

if os.name == 'posix':
    import linux
else:
    print 'Sorry, for now only linux are supported!'
    sys.exit(1)

import ps3toolchain
import psl1ght
import ps3libraries

def query_yes_no(question, default = "yes"):
    valid = {"yes" : True, "y": True, "ye" : True,
             "no" : False, "n": False }
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while 1:
        choice = raw_input(question + prompt).lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                                 "(or 'y' or 'n').\n")

# Get destination directory
dest = raw_input('Destination directory [' + linux.dir_default() + ']: ')
if dest == '':
    dest = linux.dir_default()
if dest.endswith('/'):
    dest = dest[:-1]

# Check destination
if linux.dir_exists(dest):
    if not query_yes_no('Destination directory already exists. Overwrite?',
                        'no'):
        print 'Aborted.'
        sys.exit(1)

current_dir = linux.dir_current()
base_dir = linux.dir_base(dest)
dir_name = linux.dir_toplevel(dest)

# Try to make destination directory
try:
    if not linux.dir_exists(dest):
        linux.dir_create(dest)
except:
    print 'Cannot create destination directory!'
    print 'Check write permissions.'
    sys.exit(1)

# Configure environment
print 'Some environment variables need to be set.'
if linux.file_exists(linux.at_home('.bashrc')):
    print 'I can modify your shell config file to make permanent changes'
    if query_yes_no('Can I modify your ~/.bashrc file?',
                    'yes'):
        linux.modify_bashrc(dest)
linux.set_environment(dest)

# Create build directory
linux.dir_change(current_dir)
try:
    if not linux.dir_exists('build'):
        linux.dir_create('build')
except:
    print 'Cannot create build directory.'
    sys.exit(1)
linux.dir_change('build')

# Build toolchain
ps3toolchain.download(linux.dir_change, linux.run)
ps3toolchain.build(linux.dir_change, linux.run)

# Build PSL1GHT
psl1ght.download(linux.dir_change, linux.run)
psl1ght.build(linux.dir_change, linux.run)

# Build ps3libraries
ps3libraries.download(linux.dir_change, linux.run)
ps3libraries.build(linux.dir_change, linux.run)

# Build SDL_PSL1GHT
sdlpsl1ght.download(linux.dir_change, linux.run)
sdlpsl1ght.build(linux.dir_change, linux.run)


