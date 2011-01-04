#!/usr/bin/env python

import os
import os.path

# Directory related tools
class DirectoryHelper:
    def default(self):
        raise NotImplementedError

    def exists(self, directory):
        raise NotImplementedError

    def toplevel(self, directory):
        return os.path.basename(directory)

    def base(self, directory):
        return os.path.dirname(directory)

    def current(self):
        return os.getcwd()

    def create(self, directory):
        raise NotImplementedError

    def change(self, directory):
        os.chdir(directory)

    def at_home(self, path):
        raise NotImplementedError

    def delete(self, directory):
        raise NotImplementedError

# File related tools
class FileHelper:
    def exists(self, filename):
        return os.path.isfile(filename)

    def delete(self, filename):
        raise NotImplementedError
        
# General OS tools
class OsHelper:
    def config_user(self, directory):
        raise NotImplementedError

    def set_environment(self, directory):
        # Or return False
        raise NotImplementedError

    def run(command):
        raise NotImplementedError

    # nowait not needed, for now 
    def run_nowait(command):
        self.run(command)

if __name__ == '__main__':
    print 'Nothing to test at this level...'
