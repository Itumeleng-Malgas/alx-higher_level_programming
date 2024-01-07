#!/usr/bin/python3
""" 0. What's my status? #0 """

from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print(f"Body response:\n"
        f"    - type: {type(content)}\n"
        f"    - content: {content}\n"
        f"    - utf8 content: {utf8_content}")
