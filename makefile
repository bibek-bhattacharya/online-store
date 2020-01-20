#
# Makefile for setting up Online Store API v 1.0 and running tests
#
# Assumption: python 3.5 and pip are installed.
# Instructions to install pip: https://pip.pypa.io/en/stable/installing/

VENV_NAME?=env
REQUIREMENTS_FILE?="requirements.txt"

prepare-dev-run-tests:
	pip install virtualenv
	python -m virtualenv env
	$(VENV_NAME)\Scripts\activate.bat
	pip install -r $(REQUIREMENTS_FILE)
	pytest -v
