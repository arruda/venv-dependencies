#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
Has the methods that tryes to import the modules and create symlinks for them
in the venv sitepackages folder.
"""
import os
import fileinput
from virtualenv import path_locations

def get_active_venv():
    """Checks if there is a virtualenv active
    """
    venv =os.environ.get('VIRTUAL_ENV',None)
    return venv


def get_sitepackages_path(venv):
    """Gets the path for the sitepackage in this enviroment
    """
    print venv
    return os.path.join(path_locations(venv)[1],'site-packages')

def get_easy_install_pth(sitepackage_path):
    """Gets the path for the easy-install.pth
    """
    return os.path.join(sitepackage_path,'easy-install.pth')
    
def get_module_folder(module_path):
    """Gets the folder (tail) from the module_path
    """
    return os.path.split(module_path)[1]

def module_path(string):
    """Gets the path for the module name passed in the string.
    """    
    try:
        return os.path.dirname(__import__(string).__file__)
    except ImportError:
        return None

def create_symlink(module_path, sitepackage_path):
    """Creates a symlinks for the module path to the sitepackage virtual env path
    """
    m_folder = get_module_folder(module_path)
    
    try:
        os.symlink(module_path, os.path.join(sitepackage_path,m_folder))
        return True
    except OSError:
        print "Module already linked"
        pass    
    return False
def change_easy_install_pth(easy_install_file,module_folder):
    """Change the easy-install.pth to add a new line mapping this new module.
    """
    if os.path.exists(easy_install_file):
        newline=False
        for line in fileinput.input(easy_install_file,inplace=1):
            print line[:-1]
            if not newline:
                print "./%s"%module_folder
                newline=True

