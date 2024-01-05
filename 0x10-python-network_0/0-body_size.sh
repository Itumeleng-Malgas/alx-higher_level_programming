#!/bin/bash
# displays the size of the body of the response in bytes
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n'
