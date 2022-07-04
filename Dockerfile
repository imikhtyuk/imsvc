FROM python:3.9-alpine

WORKDIR /app

ARG INPUT_DATA_URL
ARG TEMP_FILTER_THRESHOLD

ENV INPUT_DATA_URL=${INPUT_DATA_URL} \
    TEMP_FILTER_THRESHOLD=${TEMP_FILTER_THRESHOLD}

COPY app /app

ADD requirements.txt /app

RUN apk add apache2-mod-wsgi

RUN pip install -r /app/requirements.txt

EXPOSE $PORT

CMD ["sh", "-c", "gunicorn --workers 3 --bind 0.0.0.0:$PORT wsgi:app"]
