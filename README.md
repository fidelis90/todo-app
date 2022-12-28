# Python basics 

## Types of computer programs 

- Interactive programs 
  - cli 
  - desktop graphical user interface 
  - web interface (web apps)

- Non-Interactive programs 

### Goal of this project 

We want to build a basic ToDo App, that allow users check their todo list, add/remove items from the list 

#### Virtual Environment using pipenv 

brew install pipenv

mkdir ~/.virtualenvs

export WORKON_HOME=~/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

source .zshrc

pipenv --three

pipenv shell

pipenv install <module_name>
