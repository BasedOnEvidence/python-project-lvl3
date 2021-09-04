install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl --force-reinstall

package-uninstall-0.1.0:
	pip uninstall dist/page_loader-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 page_loader

page-loader:
	poetry run page-loader

tests:
	poetry run pytest -vv -s

coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests/tests.py

coverage-report:
	coverage report

.PHONY: page_loader page_loader tests
