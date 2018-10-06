export PYTHONPATH=.

PROJECT_NAME=aiohttpdemo_slackbot

# Common

all: run

run:
	@docker-compose up aiohttpdemo_slackbot_app

stop:
	@docker-compose stop

bash:
	@docker exec -it aiohttpdemo_slackbot bash

# Linters & tests

mypy:
	@docker-compose run --rm $(PROJECT_NAME)_app mypy $(PROJECT_NAME)

lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

_test:
	# todo: remove no:warnings
	@py.test -p no:warnings --cov

test: lint
	@docker-compose up test
	@docker-compose stop test


run_production:
	@docker-compose -f docker-compose.yml -f docker-compose.production.yml up
