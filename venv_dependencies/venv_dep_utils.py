#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
Has the methods that tries to import the modules and create symlinks for them
in the venv sitepackages folder.
"""
import os
import fileinput
from virtualenv import path_locations


def get_active_venv():
    """Checks if there is a virtualenv active
    """
    venv = os.environ.get('VIRTUAL_ENV', None)
    return venv


def get_sitepackages_path(venv):
    """Gets the path for the sitepackage in this enviroment
    """
    print venv
    return os.path.join(path_locations(venv)[1], 'site-packages')


def get_easy_install_pth(sitepackage_path):
    """Gets the path for the easy-install.pth
    """
    return os.path.join(sitepackage_path, 'easy-install.pth')


def get_main_module_name(module_path):
    """Gets the folder (tail) from the module_path
    """
    return os.path.split(module_path)[1]


def is_python_module(path):
    return any('__init__' in fname for fname in os.listdir(os.path.split(path)[0]))


def get_module_main_path(module_file):
    """Gets the main path for the file, that is
    sometimes a python module is inside another, and to
    make the first one work, one needs to link the main module instead of the child one
    """
    main_module_path, main_module = os.path.split(module_file)
    while 'dist-packages' not in os.path.split(main_module_path):
        # should stop if the next parent dir no longer contains a __init__ file/dir
        if not is_python_module(main_module_path) and '__init__' not in main_module:
            break
        main_module_path, main_module = os.path.split(main_module_path)

    return os.path.join(main_module_path, main_module)


def get_module_path(module_name):
    """Gets the path for the module name passed in the string.
    """
    try:
        module_file = __import__(module_name).__file__
    except ImportError:
        return None
    else:
        return get_module_main_path(module_file)


def create_symlink(module_path, sitepackage_path):
    """Creates a symlinks for the module path to the sitepackage virtual env path
    """
    main_module_name = get_main_module_name(module_path)

    try:
        os.symlink(module_path, os.path.join(sitepackage_path, main_module_name))
        return True
    except OSError:
        print "Module already linked"

    return False


def change_easy_install_pth(easy_install_file, module_folder):
    """Change the easy-install.pth to add a new line mapping this new module.
    """
    if os.path.exists(easy_install_file):
        newline = False
        for line in fileinput.input(easy_install_file, inplace=1):
            print line[:-1]
            if not newline:
                print "./%s" % module_folder
                newline = True


def link_module(module_name, site_path, easy_install_file):
    """
    Tries to link a given module, and then tries to import it.
    if any more module are missing, then tries to link them too.
    """

    module_path = get_module_path(module_name)
    if module_path is None:
        #should raise an exception?
        print "Couldn't find module '%s'" % module_name
        return
    if create_symlink(module_path, site_path):
        m_folder = get_main_module_name(module_path)
        change_easy_install_pth(easy_install_file, m_folder)
        print "Module: %s has been linked." % module_name
        try:
            __import__(module_name)
        except ImportError, e:
            missing_module = e.args[0].split('No module named')[-1]
            if missing_module != module_name:
                print "Missing module: %s" % missing_module
                link_module(missing_module, site_path, easy_install_file)
