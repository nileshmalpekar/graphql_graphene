#!/bin/bash
CONTAINER_PORT=5000
CONTAINER_HOST=127.0.0.1

gunicorn \
    -b ${CONTAINER_HOST}:${CONTAINER_PORT} \
    "my_app:create_app('flask_prod.cfg')"
