#!/bin/bash

docker-compose up -d

sleep 2

gnome-terminal --tab -- bash -c "docker exec -ti ros2-container bash"
