gendiff:
	poetry run gendiff -h

build:
	poetry build

install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test1:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test2:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

lint:
	poetry run flake8 gendiff

coverage:
	poetry run pytest --cov=gendiff/ --cov-report xml