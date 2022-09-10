#!/bin/bash

echo -n "Outcubator services are deploying..."
sudo docker compose up --detach
echo -n "Outcubator services successfully deployed."

while true; do
    echo 'Select:'
    echo '1. Generate 1000 POST request'
    echo '2. Get all applicants'
    echo '3. Get applicants by status'
    read x
    case $x in
        1)
            pip install -r /test/requirement.txt
            python3 ./test/test.py
            ;;
        2)
            curl -X GET http://host.docker.internal:8000/applicant | jq .
            ;;
        3)
            echo 'Enter appliant status'
            read stt
            curl -X GET http://host.docker.internal:8000/applicant/$stt | jq .
            ;;
        *)
            echo "Unknown option"
    echo 'Press Enter to continue.'
    esac
done
