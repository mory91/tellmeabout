.PHONY: help
help:              
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venvcheck ## Check if venv is active
venvcheck:
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif

install: venvcheck  ## Install the dependencies
	@poetry install

test: venvcheck		## Run the tests
	@tox

lint: venvcheck		## Run Black and Isort linters
	@black .
	@isort .
	@flake8 .
	@mypy .

upgrade: venvcheck	## Upgrade the dependencies
	poetry update

downgrade: venvcheck ## Downgrade the dependencies
	git checkout pyproject.toml && git checkout poetry.lock
