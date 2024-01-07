#!/usr/bin/python3
""" """


def main():
    """ Fetches https://alx-intranet.hbtn.io/status """

    url = 'https://alx-intranet.hbtn.io/status'
    import urllib.request

    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print(f"Body response:\n"
          f"    - type: {type(content)}\n"
          f"    - content: {content}\n"
          f"    - utf8 content: {utf8_content}")


if __name__ == "__main__":
    main()
