#!/bin/bash
# Use curl to send a GET request with the specified header and display the body
curl -s -H "X-School-User-Id: 98" "$1"
