#!/bin/bash
# Displays all HTTP methods the server will accept for the specified URL
curl -s -i -X OPTIONS "$1" | grep -i "^allow:" | cut -d ' ' -f2-
