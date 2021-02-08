install:
	poetry install

lint:
	poetry run flake8 aliexpress

test:
	poetry run pytest -vv --color=yes

selfcheck:
	poetry check

check: selfcheck test

build: check
	poetry build

.PHONY: install build lint selfcheck check
