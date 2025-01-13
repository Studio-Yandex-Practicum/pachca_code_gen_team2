ifneq (,$(wildcard ../../.env))
    include ../../.env
    export
endif

.PHONY: help
help:
	@echo "Команды:"
	@echo "	help	- Список всех команд"
	@echo "	test	- Запуск тестов"
	@echo "	build	- Создание библиотеки"
	@echo "	clean	- Очистка ременных файлов"
	@echo "	upload	- Загрузка библиотеки на PyPi"

test:

build: clean

	python setup_generator1.py bdist_wheel --dist-dir=../repository/
	python setup_generator2.py bdist_wheel --dist-dir=../repository/

clean: 
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/

.PHONY: upload
upload: build
	@echo "library пакет"
	@echo $$TWINE_USERNAME
	@echo $$TWINE_API_TOKEN
	TWINE_USERNAME=$$TWINE_USERNAME TWINE_PASSWORD=$$TWINE_API_TOKEN twine upload --repository testpypi ../repository/* --verbose