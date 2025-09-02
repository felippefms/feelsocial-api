.PHONY: migrations
migrations:
	docker compose exec feelsocialapi poetry run alembic revision --autogenerate

.PHONY: migrate
migrate:
	docker compose exec feelsocialapi poetry run alembic upgrade head

.PHONY: up-dependencies-only
dependencies-only:
	docker compose up feelsocialdb -d

.PHONY: run-server
run-server:
	docker compose up feelsocial_app -d
