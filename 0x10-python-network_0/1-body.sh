#!/bin/bash
# Displays the body of the response if the status code is 200
[ "$(curl -s -L -w "%{http_code}" "$1" | tail -n 1)" = "200" ] && curl -s -L "$1"
