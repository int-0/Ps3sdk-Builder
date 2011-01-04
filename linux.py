#!/usr/bin/env python

import os
import os.path
import subprocess

import oshelper

class LinuxHelper(oshelper.OsHelper):

    # Directory related tools
    class dir_helper(oshelper.DirectoryHelper):
        def default(self):
            return '/usr/local/ps3dev2'

        def exists(self, directory):
            return os.path.isdir(directory)

        def toplevel(self, directory):
            return os.path.basename(directory)

        def base(self, directory):
            return os.path.dirname(directory)

        def current(self):
            return os.getcwd()

        def create(self, directory):
            os.makedirs(directory, 0775)

        def change(self, directory):
            os.chdir(directory)

        def at_home(self, path):
            return os.path.join(os.path.expanduser('~'), path)

    # File related tools
    class file_helper(oshelper.FileHelper):
        def exists(self, filename):
            return os.path.isfile(filename)

    # File/Dir helpers
    dirs = dir_helper()
    files = file_helper()

    def config_user(self, directory):
        try:
            fd = open(at_home('.bashrc'), 'a')
        except:
            return False
        fd.write('# Added by Ps3Builder\n')
        fd.write('export PS3DEV=' + directory + '\n')
        fd.write('export PSL1GHT=' + os.path.join(directory, 'psl1ght') + '\n')
        fd.write('export PATH=$PATH:$PS3DEV/bin\n')
        fd.write('export PATH=$PATH:$PS3DEV/ppu/bin\n')
        fd.write('export PATH=$PATH:$PS3DEV/spu/bin\n')
        fd.write('# End modifications by Ps3Builder\n')
        fd.close()
        return True

    def set_environment(self, directory):
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
        pid = subprocess.Popen(command)
