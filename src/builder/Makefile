help:
	@echo "Tasks in \033[1;32mdemo\033[0m:"
	@cat Makefile

test:

build: clean

	pip install wheel
	python setup_generator1.py bdist_wheel --dist-dir=../repository/
	python setup_generator2.py bdist_wheel --dist-dir=../repository/

clean: 
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/
