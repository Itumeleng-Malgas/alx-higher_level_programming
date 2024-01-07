#!/usr/bin/python3
"""
Script to retrieve and print 10 most recent commits of a GitHub repository
"""

import requests
import sys


def get_commit(repo_name, owner_name):
    """
    Calls github api to retrieve commits.
    """

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits_data = response.json()

    for commit in commits_data:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <repository_name> <owner_name>")
        sys.exit(1)

        repo_name, owner_name = sys.argv[1], sys.argv[2]
        get_commits(repo_name, owner_name)
