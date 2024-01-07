#!/usr/bin/python3
"""
Script that takes Github credentials and uses the Github API
to display the user ID
"""

import requests
import sys
import base64

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <pesonal_access_token>")
        sys.exit(1)

    usern = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth_header = ('Basic ' + base64.b64encode(
        f"{usern}:{token}".encode('utf-8')).decode('utf-8'))

    headers = {'Authorization': auth_header}
    response = requests.get(url, headers=headers)

    user_data = response.json()
    print(user_data.get('id'))
