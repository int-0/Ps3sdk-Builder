#!/usr/bin/env python
#

import os
import sys

if os.name == 'posix':
    import linux as Linux
else:
    print 'Sorry, for now only linux are supported!'
    sys.exit(1)

import ps3toolchain
import psl1ght
import ps3libraries
import sdlpsl1ght

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

def get_destination():
    dest = raw_input('Destination directory [' + linux.dir_default() + ']: ')
    if dest == '':
        dest = linux.dirs.default()
    if dest.endswith('/'):
        dest = dest[:-1]

    # Check destination
    if linux.dirs.exists(dest):
        if not query_yes_no('Destination directory already exists. Overwrite?',
                            'no'):
            print 'Aborted.'
            sys.exit(1)

    return dest

if __name__ == '__main__':
    linux = Linux.LinuxHelper()

    dest = get_destination()
    current_dir = linux.dirs.current()
    base_dir = linux.dirs.base(dest)
    dir_name = linux.dirs.toplevel(dest)

    # Try to make destination directory
    try:
        if not linux.dirs.exists(dest):
            linux.dirs.create(dest)
    except:
        print 'Cannot create destination directory!'
        print 'Check write permissions.'
        sys.exit(1)

    # Configure environment
    print 'Some environment variables need to be set.'
    print 'I can modify your config to make permanent changes.'
    if query_yes_no('Can I modify your user configuration?', 'yes'):
        if linux.config_user(dest):
            print 'User configuration sucessfully.'
        else:
            print 'Problems configuring user data.'
            if not query_yes_no('Continue?', 'yes'):
                pass
            else:
                print 'Aborted.'
                sys.exit(1)
    linux.set_environment(dest)

    # Create build directory
    linux.dirs.change(current_dir)
    try:
        if not linux.dirs.exists('build'):
            linux.dirs.create('build')
    except:
        print 'Cannot create build directory.'
        sys.exit(1)
    linux.dirs.change('build')

    # Build toolchain
    ps3toolchain.download(linux)
    ps3toolchain.build(linux)

    # Build PSL1GHT
    psl1ght.download(linux)
    psl1ght.build(linux)

    # Build ps3libraries
    ps3libraries.download(linux)
    ps3libraries.build(linux)

    # Build SDL_PSL1GHT
    sdlpsl1ght.download(linux)
    sdlpsl1ght.build(linux)
