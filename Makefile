install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl

package-uninstall-0.1.0:
	pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 page_loader

page-loader:
	poetry run page_loader

tests:
	poetry run pytest -vv -s

coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests/tests.py

coverage-report:
	coverage report

.PHONY: page_loader page_loader tests
