install:
	poetry install

lint:
	poetry run flake8 aliexpress

selfcheck:
	poetry check

check: selfcheck

build: check
	poetry build

.PHONY: install build lint selfcheck check
