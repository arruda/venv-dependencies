import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

structurer_dir = 'venv_dependencies'
data_folder= []
data_files = ['README.rst']


setup(
    name = "venv_dependencies",
    version = "0.0.3",
    author = "Felipe Arruda Pontes",
    author_email = "contato@arruda.blog.br",
    description = ("Easy to install any dependencies in a virtualenviroment(without making symlinks by hand and etc...)"),
    license = "MIT",
    keywords = "virtualenv dependencies",
    url = "https://github.com/arruda/venv-dependencies",
    packages=['venv_dependencies'],
    scripts = ['venv_dependencies/bin/link_venv.py'],
    data_files = data_files,
    install_requires=[],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
