FROM python:3.9-alpine

WORKDIR /app

ARG INPUT_DATA_URL
ARG FILTER_THRESHOLD

ENV INPUT_DATA_URL=${INPUT_DATA_URL} \
    FILTER_THRESHOLD=${FILTER_THRESHOLD}

COPY app /app

RUN apk add apache2-mod-wsgi 

RUN pip install flask \
    requests \
    gunicorn 

EXPOSE $PORT

CMD ["sh", "-c", "gunicorn --workers 3 --bind 0.0.0.0:$PORT wsgi:app"]
