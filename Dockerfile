FROM python:3.13-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN poetry install --no-interaction --no-ansi --without dev

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 feelsocial_api.app:app