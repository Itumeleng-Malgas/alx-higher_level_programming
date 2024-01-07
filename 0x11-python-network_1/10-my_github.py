#!/usr/bin/python3
"""
Script that takes Github credentials and uses the Github API
to display the user ID
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <personal_access_token>")
        sys.exit(1)

    usern, token = sys.argv[1], sys.argv[2]
    url = 'https://api.github.com/user'
:x
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    user_data = response.json()
    print(user_data.get('id'))
