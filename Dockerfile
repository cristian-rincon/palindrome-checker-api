FROM python:3.9-alpine AS base
WORKDIR /app
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY ./api /app/api

FROM base AS dev
CMD ["uvicorn", "api.main:app" , "--host", "0.0.0.0", "--reload"]

FROM base AS prod
CMD ["uvicorn", "api.main:app" , "--host", "0.0.0.0"]
