#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
Executes the methos in utils.py
This file should be running under the original python,
not an env one
"""
import sys
from venv_dependencies.venv_dep_utils import (
    get_active_venv,
    get_sitepackages_path,
    get_easy_install_pth,
    link_module
)


def main(modules):
    venv = get_active_venv()
    if venv is None:
        print "No virtual envs"
        return
    site_path = get_sitepackages_path(venv)
    easy_install_file = get_easy_install_pth(site_path)

    for m in modules:
        link_module(m, site_path, easy_install_file)


if __name__ == "__main__":
    modules = sys.argv[1:]
    if modules != []:
        main(modules)
