#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print(content)
