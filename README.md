# Fasterthan Blog: pre-commit hooks for a python project

Demonstration project, written in the context of an article of the
[fasterthan blog](https://blog.fasterthan.fr/), to explain how to set up pre-commit
hooks for a Python / Django project.

## Requirements

| Name   | Version |
|--------|---------|
| Python | 3.10    |
| Django | 5.0.3   |

## Install

Create a `venv` (Python 3.10 has been used to write the article):
```
python3.10 -m venv ~/.venvs/blog_entry_pre_commit_ci
```
Install the requirements and setup pre-commit hooks:
```
pip install -r requirements.txt
pre-commit install
```
To run the pre-commit hooks on all the project:
```console
foo@bar:~$ pre-commit run --all-file
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
black (python)...........................................................Passed
isort (python)...........................................................Passed
flake8 (python)..........................................................Passed
bandit (python)..........................................................Passed
Check forgotten migrations (django)......................................Passed
Check outdated po files (django).........................................Passed
```

## Run the tests

```
pytest .
```
