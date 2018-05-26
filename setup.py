"""Python script setting up the project locally.

Must be executed from the project directory.

Installs needed OS packages. Sorry, only apt supported at the moment.
"""
from __future__ import print_function

import os

from subprocess import call


ENV_NAME = 'EnglishWordsGameEnv'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VIRTUALENV_PATH = os.path.join(PROJECT_DIR, ENV_NAME)
ACTIVATE_PATH = os.path.join(VIRTUALENV_PATH, 'bin', 'activate_this.py')
PIP_PATH = os.path.join(VIRTUALENV_PATH, 'bin', 'pip')
PYTHON_PATH = os.path.join(VIRTUALENV_PATH, 'bin', 'python')

OS_PACKAGES = [
    'python-dev',
    'git',  # need to install python packages from github
    'python-pip',
    'python-virtualenv',
]


def sudo_apt_get(*args):
    "apt-get helper"
    sudo_cmd = ['sudo', 'apt-get']
    call(sudo_cmd + list(args))


def apt_get_install():
    sudo_apt_get('update')
    for package_name in OS_PACKAGES:
        sudo_apt_get('install', '-y', package_name)


def setup_virtualenv():
    call(['virtualenv', ENV_NAME])


def setup_python_requirements():
    call([PIP_PATH, 'install', '-r', 'requirements.txt'])


def setup_django_project():
    call([PYTHON_PATH, './english_words_game/manage.py', 'syncdb', '--noinput'])
    call([PYTHON_PATH, './english_words_game/manage.py', 'migrate'])
    call([PYTHON_PATH, '-c', '"import nltk; nltk.download(\'wordnet\')"'])


def running_instructions():
    print("""Congratulations! You've set up the English Word Game locally.

There're just few steps in shell to start development server:

$ source {virtualenv}
$ cd english_words_game
$ ./manage.py runserver

After that you should be able to open project in browser at http://localhost:8000/
""".format(
        virtualenv=os.path.join(VIRTUALENV_PATH, 'bin', 'activate'),
    ))


if __name__ == '__main__':
    apt_get_install()
    setup_virtualenv()
    setup_python_requirements()
    setup_django_project()
    running_instructions()
