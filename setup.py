import os
from distutils.core import setup

setup(
    name = "venv_dependencies",
    version = "0.0.7",
    author = "Felipe Arruda Pontes",
    author_email = "contato@arruda.blog.br",
    description = ("Easy to install any dependencies in a virtualenviroment(without making symlinks by hand and etc...)"),
    license = 'LICENSE',
    keywords = "virtualenv dependencies",
    url = "https://github.com/arruda/venv-dependencies",
    packages=['venv_dependencies'],
    scripts = ['bin/link_venv.py'],
    data_files = [],
    install_requires=['virtualenv'],
    long_description=open('README.txt').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
