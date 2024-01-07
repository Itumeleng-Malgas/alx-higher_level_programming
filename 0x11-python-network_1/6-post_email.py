#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
to the URL with the email as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)
