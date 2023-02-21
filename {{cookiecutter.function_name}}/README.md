{{ cookiecutter.project_name }}
===============================================

Project for function `{{ cookiecutter.function_name }}`.

## Requirements

- Python 3.10.6 (in [`.python-version`](./.python-version)): Recommended to use [pyenv](https://github.com/pyenv/pyenv) to manage your python versions.
- **Pipenv**: See how to install pipenv [here](https://pipenv.pypa.io/en/latest/#install-pipenv-today).
- **Pytest**: See more about pytest [here](https://docs.pytest.org/en/6.2.x/).

## Installation

```
$ make install
```

### `Pipfile.lock`

This file is used to lock the versions of the dependencies. It is generated automatically when you run `make install`.

You **must commit this file** to your version control system.

## Lint

```
$ make lint
```

## Tests

```
$ make test
```

### How to test?

We are using [pytest](https://docs.pytest.org/en/stable/) to run our tests. Just add tests in the same folder as the code you want to test.

## Deploy

Build dist dir to be deployed:

```
$ make build
```

Github actions will just need a Service Account with role [`roles/cloudfunctions.admin`](https://cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.admin).

Generate a SA, a key file and add a secret called `SERVICE_ACCOUNT_CREDENTIALS_JSON` in Github Secrets with the content of the key file.

## Running locally

```shell
$ make run
```
