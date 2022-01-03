# syntax=docker/dockerfile:1
FROM python:3.9 AS base
WORKDIR /app
RUN python3 -m pip install --no-cache-dir pipenv==2021.11.23

FROM base AS prod
COPY Pipfile .
# COPY Pipfile.lock .
RUN python3 -m pipenv install
COPY plyanging plyanging
COPY darlyng darlyng
COPY scripts scripts
# Set .env by supplying --env-file when calling docker run or copy the .env file into the container when creating it.
CMD [ "/bin/bash", "scripts/container_run.sh" ]