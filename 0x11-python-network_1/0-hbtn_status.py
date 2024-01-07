#!/usr/bin/python3
"""
A simple script to make an HTTP request to https://alx-intranet.hbtn.io/status
and print information about the response.
"""
import urllib.request

if __name__ == "__main__":
    # Open the specified URL and read the response
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content = resp.read()
        utf8_content = content.decode('utf-8')

        # Print information about the response
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", utf8_content)
