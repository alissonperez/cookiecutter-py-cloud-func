
install:
	pipenv install --dev

lint:
	pipenv run flake8 .

test:
	pipenv run pytest

run:
	pipenv run functions-framework --target {{ cookiecutter.function_name }} --debug

clean-dist:
	rm -rf dist

build: clean-dist
	mkdir dist
	pipenv requirements > ./dist/requirements.txt
	cp README* ./dist/
	cp main.py ./dist/
	cp -R ./{{ cookiecutter.function_name }} ./dist/
