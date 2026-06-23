#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "api_advanced:v1.0 (by /u/api_advanced_project)"}
    params = {"limit": 10}
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)