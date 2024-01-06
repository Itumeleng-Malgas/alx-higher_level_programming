#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and cause the server to respond with "You got me!"
curl -s -X PUT -L -d "user_id=1337" "0.0.0.0:5000/catch_me" > /dev/null 2>&1
