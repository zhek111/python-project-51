install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

all:
	poetry build
	poetry publish --dry-run
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 page_loader tests

test:
	poetry run pytest -s

test-cov:
	poetry run pytest --cov=page_loader --cov-report xml

