help:
	@echo "Makefile commands"
	@echo "install - Установка зависимостей"
	@echo "test - Запуск автотестов"

install:
	pip install -r requirements.txt

run_test:
	python3 -m pytest