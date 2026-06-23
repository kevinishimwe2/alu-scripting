#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (custom) api_advanced/1.0"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print("None")
        return
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)