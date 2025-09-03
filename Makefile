.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	docker compose exec feelsocial_app poetry run alembic revision --autogenerate

.PHONY: migrate
migrate:
	docker compose exec feelsocial_app poetry run alembic upgrade head

.PHONY: up-dependencies-only
up-dependencies-only:
	docker compose up feelsocialdb -d

.PHONY: run-server
run-server:
	docker compose up feelsocial_app -d
