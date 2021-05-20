#!/bin/bash

flask db migrate

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "Upgrade command fail"
    echo "Waiting for MYSQL to start, retrying in 5 secs..."
    sleep 5
done

flask run --host=0.0.0.0