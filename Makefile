gendiff:
	poetry run gendiff -h

build:
	poetry build

install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test1:
	poetry run gendiff /python_learn/projects/python-project-lvl2/tests/fixtures/file1.json /python_learn/projects/python-project-lvl2/tests/fixtures/file2.json

make lint:
	poetry run flake8 gendiff