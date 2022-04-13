gendiff:
	poetry run gendiff -h

build:
	poetry build

install:
	python3 -m pip install --user dist/*.whl

test1:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json