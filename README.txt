===================================
Virtual Enviroment Dependencies
===================================

About:
-----------------------------------

This app helps to create symbolics links for any module from your original python to your current virtual enviroment.
This way you don't need to do the links by your self using bash, just use this app.


Usage:
-----------------------------------
You use the command::

    link_venv "module1" "module2"... "moduleN"
Ex:
Enable gtk to work in the virtualenv::

    link_venv.py "gtk" "gobject" "glib" "cairo" "gio" "pango"

Install:
-----------------------------------
pip install -e git+https://github.com/arruda/venv-dependencies.git#egg=venv_dependencies


License:
-----------------------------------
This software is distributed using MIT license, see LICENSE file for more details.
