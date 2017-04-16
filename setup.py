from distutils.core import setup

setup(
    name="venv_dependencies",
    version="1.0.8",
    author="Felipe Arruda Pontes",
    author_email="contato@arruda.blog.br",
    description=("Easy to link OS dependencies in a virtualenviroment (without making symlinks yourself)"),
    license='LICENSE',
    keywords="virtualenv dependencies opencv",
    url="https://github.com/arruda/venv-dependencies",
    packages=['venv_dependencies'],
    scripts=['bin/link_venv.py'],
    data_files=[],
    install_requires=['virtualenv'],
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
