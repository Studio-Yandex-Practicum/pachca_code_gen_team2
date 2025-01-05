help:
	@echo "Tasks in \033[1;32mdemo\033[0m:"
	@cat Makefile

lint:
	mypy src --ignore-missing-imports
	flake8 src --ignore=$(shell cat .flakeignore)

dev:
	pip install -e .

test: dev


build: clean

	pip install wheel
	python setup.py bdist_wheel --dist-dir=../repository/

clean: 
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/
