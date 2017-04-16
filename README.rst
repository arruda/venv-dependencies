===================================
Virtual Enviroment Dependencies
===================================

About
-----------------------------------

This app helps to create symbolics links for any module from your
OS python to your current virtual enviroment. This way you don't
need to do the links by yourself using bash, just use this app.


Usage
-----------------------------------

You use the command::

    link_venv "module1" "module2"... "moduleN"

Example: Enable OpenCV to work in the virtualenv::

    link_venv.py "cv2"


Install
-----------------------------------

::

  pip install venv-dependencies


License:
-----------------------------------

This software is distributed using MIT license, see LICENSE file for
more details.
