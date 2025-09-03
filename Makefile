.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	docker compose exec feelsocial_api poetry run alembic revision --autogenerate

.PHONY: migrate
migrate:
	docker compose exec feelsocial_api poetry run alembic upgrade head

.PHONY: up-dependencies-only
up-dependencies-only:
	docker compose up --force-recreate feelsocialdb

.PHONY: run-dev
run-dev:
	poetry run uvicorn --host 0.0.0.0 --port 8000 feelsocial_api.app:app --reload

.PHONY: run-server
run-server:
	docker compose up feelsocial_api
