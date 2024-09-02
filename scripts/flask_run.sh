#!/bin/bash
CONTAINER_PORT=5000
CONTAINER_HOST=127.0.0.1

FLASK_APP=app.py \
    FLASK_ENV=development \
    flask run \
    -h ${CONTAINER_HOST} \
    -p ${CONTAINER_PORT}
