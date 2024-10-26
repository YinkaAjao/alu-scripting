#!/usr/bin/python3
"""Script that fetches titles of the top 10 hot posts for a given subreddit."""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, it prints None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    # Check if subreddit is valid
    if response.status_code == 200:
        json_data = response.json().get('data', {}).get('children', [])
        if json_data:
            for post in json_data:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    else:
        print(None)

