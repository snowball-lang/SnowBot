#/usr/bin/env bash
NAME="snowbotmachine"

docker build -t $NAME .

# to remove the container:
# docker rmi $NAME