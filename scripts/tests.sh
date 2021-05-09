#!/bin/bash
# run inside a anunbis_backend docker container
coverage run --source=app -m unittest discover -s tests/ -v
coverage report
coverage xml
coverage html
