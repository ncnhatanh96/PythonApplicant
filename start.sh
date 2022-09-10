#!/bin/bash

echo -n "Outcubator services are deploying..."
#sudo docker compose up --detach

#until  $(curl -f http://127.0.0.1:8001); do echo 'Waiting for deploy process'; sleep 1; done

echo -n "Outcubator services successfully deployed."
generate_post_data()
{
  cat <<EOF
{
    "name": "$name",
    "email": "$email",
    "screenName": "$screenName",
}
EOF
}
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
