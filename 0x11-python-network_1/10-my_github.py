#!/usr/bin/python3
"""
Script that takes Github credentials and uses the Github API
to display the user ID
"""

import requests
import sys
import base64

if __name__ == "__main__":

    usern = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'

    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    user_data = response.json()
    print(user_data.get('id'))
