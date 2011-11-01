#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
Executes the methos in utils.py
This file should be running under the original python,
not an env one
"""
import sys
from venv_dependencies.venv_dep_utils import *

def main(modules):
    venv = get_active_venv()
    if venv is None:
        print "No virtual envs"
        #raise an exception here
        return
    site_path = get_sitepackages_path(venv)
    easy_install_file = get_easy_install_pth(site_path)

    for m in modules:
        m_path = module_path(m)
        if m_path is None:
            #should raise an exception?
            continue
        if create_symlink(m_path,site_path):    
            m_folder = get_module_folder(m_path)
            change_easy_install_pth(easy_install_file, m_folder)
            print "Module: %s has been linked." % m

if __name__ == "__main__":
    modules = sys.argv[1:]
    if modules != []:
        main(modules)
    
