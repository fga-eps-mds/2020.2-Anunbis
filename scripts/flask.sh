#!/bin/bash

flask db migrate

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "upgrade command failed, retrying in 5 secs..."
    sleep 5
done

flask run --host=0.0.0.0