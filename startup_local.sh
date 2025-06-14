#!/bin/bash
mkdir -p ./prometheus && rm -f ./prometheus/*
export CONFIGURATION_FILE=$(PWD)/application.cfg
PROMETHEUS_MULTIPROC_DIR=./prometheus gunicorn "src:create_app()" -c manage.py