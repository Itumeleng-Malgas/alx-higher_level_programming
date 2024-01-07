#!/usr/bin/python3
""" """

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print(f"Body response:\n"
          f"    - type: {type(content)}\n"
          f"    - content: {content}\n"
          f"    - utf8 content: {utf8_content}")
